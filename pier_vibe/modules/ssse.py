"""SSSE: Sub-Surface Scour Engine - Module 01.

Computes scour depth evolution around bridge piers.
"""

import numpy as np


class SSSE:
    """Sub-Surface Scour Engine."""
    
    def __init__(self, pier_diameter: float = 3.5, water_depth: float = 25.0):
        self.D_pier = pier_diameter
        self.y = water_depth
        self.C_s = 0.025  # Scour rate coefficient
        
    def compute_scour_rate(self, u_star: float, d_50: float = 0.5, 
                           D_s: float = 0.0, D_s_max: float = 4.2) -> float:
        """Melville-Coleman scour rate equation.
        
        ∂z_s/∂t = C_s · u* · f(d_s/d_50) · g(y/D_pier) · [1 - D_s/D_s,max]
        """
        f_grain = self._grain_size_factor(d_50)
        g_depth = self._depth_factor()
        
        return self.C_s * u_star * f_grain * g_depth * (1 - D_s / D_s_max)
    
    def _grain_size_factor(self, d_50: float) -> float:
        """Grain size correction f(d_s/d_50)."""
        if d_50 <= 0.5:
            return 1.0
        return 0.5 + 0.5 * (0.5 / d_50)
    
    def _depth_factor(self) -> float:
        """Depth correction g(y/D_pier)."""
        ratio = self.y / self.D_pier
        if ratio <= 1.0:
            return ratio
        return 1.0
    
    def compute_horseshoe_amplification(self, Re: float) -> float:
        """Horseshoe vortex bed shear amplification α_v."""
        if Re < 1e5:
            return 2.0
        elif Re < 1e6:
            return 2.5
        return 3.0
    
    def compute_equilibrium_depth(self, u: float, d_50: float = 0.5) -> float:
        """HEC-18 equilibrium scour depth."""
        # Simplified HEC-18 formula
        Fr = u / np.sqrt(9.81 * self.y)
        return 2.0 * self.D_pier * Fr**0.65 * (d_50/0.5)**(-0.2)
