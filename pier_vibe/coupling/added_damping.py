"""Hydrodynamic added damping computation."""

import numpy as np


class AddedDamping:
    """Added damping from radiation and viscous effects."""
    
    def __init__(self, rho: float = 1025.0):
        self.rho = rho
        
    def radiation_damping(self, omega: float, D: float, L: float) -> float:
        """Radiation damping from wave generation."""
        # Simplified radiation damping
        return 0.5 * self.rho * omega * D**2 * L
    
    def viscous_damping(self, D: float, L: float, u: float, C_d: float = 1.0) -> float:
        """Viscous drag damping."""
        return 0.5 * self.rho * C_d * D * L * abs(u)
    
    def total_added_damping(self, omega: float, D: float, L: float, u: float) -> float:
        """Total added damping = radiation + viscous."""
        return self.radiation_damping(omega, D, L) + self.viscous_damping(D, L, u)
    
    def damping_ratio(self, C_a: float, M: float, K: float) -> float:
        """Damping ratio ζ = C_a / (2·√(K·M))"""
        return C_a / (2 * np.sqrt(K * M))
