import unittest
from run_analysis import load, two_way_beta

class AnalysisTests(unittest.TestCase):
    def test_panel_shape_and_unique_keys(self):
        rows = load()
        self.assertEqual(len(rows), 64)
        self.assertEqual(len({(r["region"],r["year"]) for r in rows}),64)
    def test_two_way_estimator_is_finite(self):
        self.assertTrue(-10 < two_way_beta(load()) < 10)

if __name__=="__main__":
    unittest.main()
