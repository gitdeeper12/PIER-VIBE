"""Unit tests for EFGL (Elastic Fatigue Governance Lock)."""

import unittest
import numpy as np
from pier_vibe.modules.efgl import EFGL


class TestEFGL(unittest.TestCase):
    """Test cases for EFGL module."""
    
    def setUp(self):
        self.efgl = EFGL(detail_category="B")
    
    def test_cycles_to_failure(self):
        N = self.efgl.compute_cycles_to_failure(stress_amplitude_MPa=100)
        self.assertGreater(N, 0)
    
    def test_fatigue_damage(self):
        damage = self.efgl.compute_fatigue_damage([1000], [100])
        self.assertGreater(damage, 0)
        self.assertLessEqual(damage, 1.0)
    
    def test_goodman_correction(self):
        sigma_eq = self.efgl.goodman_correction(sigma_a=100, sigma_m=50, sigma_UTS=500)
        self.assertGreater(sigma_eq, 100)
    
    def test_rainflow_counting(self):
        stress = [50, 80, 60, 90, 40, 70, 55]
        cycles, amps = self.efgl.rainflow_counting(stress)
        self.assertEqual(len(cycles), len(amps))


if __name__ == '__main__':
    unittest.main()
