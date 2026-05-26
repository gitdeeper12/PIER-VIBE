"""Unit tests for AI modules (PINN, BSHI)."""

import unittest
import numpy as np
from pier_vibe.ai import PINNScourForecaster, PINNFatigueForecaster, BSHICalculator


class TestAIModules(unittest.TestCase):
    """Test cases for AI modules."""
    
    def test_pinn_scour(self):
        pinn = PINNScourForecaster.from_pretrained()
        pred = pinn.predict(np.random.randn(100), hours=72)
        self.assertGreater(pred, 0)
        self.assertAlmostEqual(pinn.RMSE_72H, 0.08, places=2)
    
    def test_pinn_fatigue(self):
        pinn = PINNFatigueForecaster.from_pretrained()
        pred = pinn.predict(np.random.randn(100), hours=72)
        self.assertGreater(pred, 0)
        self.assertAlmostEqual(pinn.MAE_72H, 0.028, places=3)
    
    def test_bshi_calculator(self):
        bshi = BSHICalculator.from_pretrained()
        value = bshi.compute(scour_depth=1.8, fatigue_damage=0.35, freq_drift=2.1)
        self.assertGreater(value, 0)
        self.assertLessEqual(value, 1.0)
        self.assertAlmostEqual(bshi.PRECISION, 0.97, places=2)
    
    def test_bshi_risk_classification(self):
        bshi = BSHICalculator.from_pretrained()
        risk = bshi.classify_risk(0.90)
        self.assertEqual(risk, "normal")
        risk = bshi.classify_risk(0.80)
        self.assertEqual(risk, "elevated")
        risk = bshi.classify_risk(0.70)
        self.assertEqual(risk, "critical")


if __name__ == '__main__':
    unittest.main()
