"""Horseshoe vortex dynamics at pier-bed interface."""

import numpy as np


class HorseshoeVortex:
    """Horseshoe vortex system around bridge pier."""
    
    def __init__(self):
        self.alpha_v_base = 2.5  # Base amplification factor
        
    def amplification_factor(self, Re: float, y_D: float) -> float:
        """Bed shear amplification α_v = τ_b,max/τ_b,0"""
        # Reynolds number effect
        if Re < 1e5:
            Re_factor = 2.0
        elif Re < 1e6:
            Re_factor = 2.5
        else:
            Re_factor = 3.0
        
        # Depth ratio effect
        depth_factor = 1.0 if y_D > 1.0 else y_D
        
        return Re_factor * depth_factor
    
    def shear_stress_distribution(self, tau_0: float, r: float, 
                                  D: float, theta: float) -> float:
        """τ_b(θ, r) = τ_b,0·α_v·exp(-β·(r-D/2)/D)·f(θ)"""
        beta = 2.5
        decay = np.exp(-beta * (r - D/2) / D)
        angular = self._angular_distribution(theta)
        return tau_0 * self.alpha_v_base * decay * angular
    
    def _angular_distribution(self, theta: float) -> float:
        """Angular distribution f(θ) around pier."""
        return np.cos(theta / 2) if abs(theta) < np.pi/2 else 0.5
    
    def vortex_strength(self, u_inf: float, D: float, Re: float) -> float:
        """Horseshoe vortex circulation."""
        # Simplified estimation
        return 0.5 * u_inf * D * (1 - 1/np.sqrt(Re))
