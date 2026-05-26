"""HEC-18 equilibrium scour depth prediction."""

import numpy as np


class EquilibriumDepth:
    """HEC-18 live-bed equilibrium scour depth."""
    
    def __init__(self):
        pass
    
    def compute(self, y: float, D: float, Fr: float, d_50: float) -> float:
        """D_s,max = 2.0·D·Fr^0.65·(d_50/0.5)^-0.2"""
        return 2.0 * D * Fr**0.65 * (d_50 / 0.5)**(-0.2)
    
    def froude_number(self, u: float, y: float) -> float:
        """Fr = u / √(g·y)"""
        return u / np.sqrt(9.81 * y)
    
    def clear_water_scour(self, y: float, D: float, 
                          u_c: float, u: float) -> float:
        """Clear-water scour (u < u_c)."""
        ratio = u / u_c
        if ratio >= 1.0:
            return 0
        return 2.0 * D * (ratio)**0.5
    
    def critical_velocity(self, y: float, d_50: float) -> float:
        """Critical velocity for sediment motion."""
        return 6.0 * y**0.167 * d_50**0.333
