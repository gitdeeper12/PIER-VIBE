"""Unit tests for SSSE (Sub-Surface Scour Engine)."""

import unittest
import numpy as np
from pier_vibe.modules.ssse import SSSE


class TestSSSE(unittest.TestCase):
    """Test cases for SSSE module."""
    
    def setUp(self):
        self.ssse = SSSE(pier_diameter=3.5, water_depth=25.0)
    
    def test_scour_rate(self):
        rate = self.ssse.compute_scour_rate(u_star=0.1, d_50=0.5, D_s=1.0, D_s_max=4.2)
        self.assertGreater(rate, 0)
        self.assertLess(rate, 0.1)
    
    def test_horseshoe_amplification(self):
        amp = self.ssse.compute_horseshoe_amplification(Re=1e6)
        self.assertGreaterEqual(amp, 2.0)
        self.assertLessEqual(amp, 3.5)
    
    def test_equilibrium_depth(self):
        depth = self.ssse.compute_equilibrium_depth(u=2.0, d_50=0.5)
        self.assertGreater(depth, 0)
    
    def test_grain_size_factor(self):
        factor = self.ssse._grain_size_factor(0.5)
        self.assertEqual(factor, 1.0)
        factor = self.ssse._grain_size_factor(1.0)
        self.assertLess(factor, 1.0)
    
    def test_depth_factor(self):
        factor = self.ssse._depth_factor()
        self.assertGreater(factor, 0)


if __name__ == '__main__':
    unittest.main()
