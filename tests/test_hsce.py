"""Unit tests for HSCE (Hydro-Structural Coupling Evaluator)."""

import unittest
import numpy as np
from pier_vibe.modules.hsce import HSCE


class TestHSCE(unittest.TestCase):
    """Test cases for HSCE module."""
    
    def setUp(self):
        self.hsce = HSCE(pier_diameter=3.5, water_depth=25.0)
    
    def test_morison_force(self):
        force = self.hsce.compute_morison_force(u=2.0, du_dt=0.5)
        self.assertGreater(force, 0)
    
    def test_added_mass(self):
        Ma = self.hsce.compute_added_mass(L_sub=20.0)
        self.assertGreater(Ma, 0)
    
    def test_froude_number(self):
        Fr = self.hsce.compute_froude_number(u=2.0)
        self.assertGreater(Fr, 0)
    
    def test_wave_number(self):
        k = self.hsce.compute_wave_number(T=6.0)
        self.assertGreater(k, 0)


if __name__ == '__main__':
    unittest.main()
