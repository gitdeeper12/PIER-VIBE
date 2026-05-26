"""Horseshoe vortex amplification factors."""

import numpy as np


class HorseshoeAmplification:
    """Horseshoe vortex bed shear amplification."""
    
    def __init__(self):
        self.alpha_v_base = 2.5
        
    def amplification(self, Re: float, y_D: float) -> float:
        """τ_b,max/τ_b,0 = α_v(Re, y/D)"""
        # Reynolds number effect
        if Re < 1e5:
            Re_factor = 2.0
        elif Re < 1e6:
            Re_factor = 2.5
        else:
            Re_factor = 3.0
        
        # Depth ratio effect
        depth_factor = 1.0 if y_D >= 1.0 else y_D
        
        return Re_factor * depth_factor
    
    def spatial_distribution(self, theta: float, r: float, D: float) -> float:
        """Normalized bed shear distribution around pier."""
        beta = 2.5
        # Radial decay
        radial = np.exp(-beta * (r - D/2) / D)
        # Angular variation
        angular = self._angular_function(theta)
        return radial * angular
    
    def _angular_function(self, theta: float) -> float:
        """Angular distribution f(θ)."""
        theta_deg = np.degrees(theta)
        if abs(theta_deg) < 90:
            return np.cos(np.radians(theta_deg) / 2)
        else:
            return 0.5
    
    def vortex_core_radius(self, D: float, Re: float) -> float:
        """Horseshoe vortex core radius."""
        return 0.1 * D / np.sqrt(Re / 1e6)
