"""Melville-Coleman scour rate equation implementation."""

import numpy as np


class MelvilleColeman:
    """Melville-Coleman scour depth evolution model."""
    
    def __init__(self, C_s: float = 0.025):
        self.C_s = C_s  # Scour rate coefficient
        
    def scour_rate(self, u_star: float, d_50: float, y: float, D_pier: float,
                   D_s: float, D_s_max: float) -> float:
        """∂z_s/∂t = C_s·u*·f(d_s/d_50)·g(y/D_pier)·[1 - D_s/D_s,max]"""
        f_grain = self._grain_factor(d_50)
        g_depth = self._depth_factor(y, D_pier)
        return self.C_s * u_star * f_grain * g_depth * (1 - D_s / D_s_max)
    
    def _grain_factor(self, d_50: float) -> float:
        """Grain size correction factor f(d_s/d_50)."""
        if d_50 <= 0.5:
            return 1.0
        return 0.5 + 0.5 * (0.5 / d_50)
    
    def _depth_factor(self, y: float, D_pier: float) -> float:
        """Depth correction factor g(y/D_pier)."""
        ratio = y / D_pier
        return min(ratio, 1.0)
    
    def time_to_equilibrium(self, u_star: float, D_s_max: float) -> float:
        """Time to reach equilibrium scour depth."""
        return D_s_max / (self.C_s * u_star)
