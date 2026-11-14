#!/usr/bin/env python3
"""Script reproducible, solo Python estándar. Ningún dato real de INE o FRONTUR."""
from __future__ import annotations
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / "data" / "synthetic_panel.csv"
OUT = BASE / "outputs"

def load():
    with SOURCE.open(encoding="utf-8", newline="") as f:
        records = list(csv.DictReader(f))
    required = {"region", "year", "population", "tourists", "nominal_wage", "cpi"}
    assert records and required.issubset(records[0]), "Columnas necesarias ausentes"
    for r in records:
        r["year"] = int(r["year"])
        for col in ("population", "tourists", "nominal_wage", "cpi"):
            r[col] = float(r[col])
            assert r[col] > 0, (col, r)
        r["real_wage"] = r["nominal_wage"] / (r["cpi"] / 100.0)
        r["intensity"] = r["tourists"] / r["population"]
        r["x"] = math.log(1.0 + r["intensity"])
        r["y"] = math.log(r["real_wage"])
    keys = [(r["region"], r["year"]) for r in records]
    assert len(keys) == len(set(keys)), "Región-año duplicado"
    return records

def two_way_beta(records):
    """Coeficiente descriptivo de pendiente OLS con dos efectos fijos en panel balanceado."""
    regions = sorted({r["region"] for r in records})
    years = sorted({r["year"] for r in records})
    assert len(records) == len(regions) * len(years), "Panel no balanceado"
    assert all(sum(r["region"] == reg for r in records) == len(years) for reg in regions)
    rx = {reg: sum(r["x"] for r in records if r["region"] == reg) / len(years) for reg in regions}
    ry = {reg: sum(r["y"] for r in records if r["region"] == reg) / len(years) for reg in regions}
    tx = {year: sum(r["x"] for r in records if r["year"] == year) / len(regions) for year in years}
    ty = {year: sum(r["y"] for r in records if r["year"] == year) / len(regions) for year in years}
    mx = sum(r["x"] for r in records) / len(records)
    my = sum(r["y"] for r in records) / len(records)
    demeaned = [
        (r["x"] - rx[r["region"]] - tx[r["year"]] + mx,
         r["y"] - ry[r["region"]] - ty[r["year"]] + my)
        for r in records
    ]
    numerator = sum(x * y for x, y in demeaned)
    denominator = sum(x * x for x, _ in demeaned)
    assert denominator > 1e-12, "Sin variación para estimar beta"
    return numerator / denominator

def make_chart(records):
    """Genera figura SVG de salarios REALES de dos regiones sintéticas."""
    chosen = ("Baleares_SIM", "Canarias_SIM")
    selected = sorted((r for r in records if r["region"] in chosen), key=lambda r:(r["region"], r["year"]))
    lo = min(r["real_wage"] for r in selected) - 700
    hi = max(r["real_wage"] for r in selected) + 700
    def px(year): return 70 + (year - 2017) * 74
    def py(wage): return 280 - (wage - lo) / (hi - lo) * 210
    lines=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 690 340">',
           '<rect width="690" height="340" fill="white"/>',
           '<text x="70" y="30" font-family="sans-serif" font-size="17">Salario real anual (datos sintéticos)</text>',
           '<path d="M70 70 L70 280 L590 280" fill="none" stroke="black"/>']
    for i,name in enumerate(chosen):
        points=" ".join(f'{px(r["year"]):.1f},{py(r["real_wage"]):.1f}' for r in selected if r["region"]==name)
        color=("steelblue","darkorange")[i]
        lines.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>')
        lines.append(f'<text x="590" y="{49+i*22}" font-family="sans-serif" font-size="13" fill="{color}">{name}</text>')
    for year in range(2017,2025):
        lines.append(f'<text x="{px(year):.0f}" y="302" text-anchor="middle" font-family="sans-serif" font-size="11">{year}</text>')
    lines.append('<text x="70" y="328" font-family="sans-serif" font-size="11">SIMULADO: no representa salarios reales de las regiones españolas.</text>')
    lines.append('</svg>')
    (OUT / "figure_real_wage.svg").write_text("\n".join(lines)+"\n",encoding="utf-8")

def run():
    rows = load()
    OUT.mkdir(parents=True, exist_ok=True)
    beta = two_way_beta(rows)
    summary = {
        "dataset":"100% sintético",
        "rows":len(rows),
        "regions":len(set(r["region"] for r in rows)),
        "years":sorted(set(r["year"] for r in rows)),
        "year_2020_included":any(r["year"]==2020 for r in rows),
        "beta_two_way_fe_descriptive":round(beta,6),
        "interpretation":"asociación condicional; NO es causal; x=log(1+turistas/población)"
    }
    (OUT/"summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    with (OUT/"regional_2024.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f, lineterminator="\n")
        w.writerow(["region","year","real_wage","tourists_per_resident"])
        for r in sorted((r for r in rows if r["year"]==2024),key=lambda r:r["region"]):
            w.writerow([r["region"],r["year"],f'{r["real_wage"]:.2f}',f'{r["intensity"]:.4f}'])
    make_chart(rows)
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=="__main__":
    run()
