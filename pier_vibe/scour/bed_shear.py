"""Bed shear stress computation for sediment transport."""

import numpy as np


class BedShear:
    """Bed shear stress τ_b at pier-bed interface."""
    
    def __init__(self, rho: float = 1025.0):
        self.rho = rho
        
    def shear_velocity(self, tau_b: float) -> float:
        """u* = √(τ_b/ρ)"""
        return np.sqrt(tau_b / self.rho)
    
    def bed_shear(self, u: float, z: float, z0: float = 0.01) -> float:
        """τ_b = ρ·u*² from log law"""
        # von Karman constant
        kappa = 0.41
        u_star = kappa * u / np.log(z / z0)
        return self.rho * u_star**2
    
    def shields_parameter(self, tau_b: float, d_50: float, 
                          rho_s: float = 2650.0) -> float:
        """Shields parameter θ = τ_b / [(ρ_s - ρ)g·d_50]"""
        g = 9.81
        denominator = (rho_s - self.rho) * g * d_50 / 1000
        return tau_b / denominator if denominator > 0 else 0
    
    def critical_shields(self) -> float:
        """Critical Shields parameter θ_cr ≈ 0.047"""
        return 0.047
    
    def is_scouring(self, u_star: float, d_50: float) -> bool:
        """Check if scour is initiated."""
        # Critical shear velocity for sediment motion
        u_star_crit = 0.03 * np.sqrt((2650 - self.rho) / self.rho * 9.81 * d_50 / 1000)
        return u_star > u_star_crit
