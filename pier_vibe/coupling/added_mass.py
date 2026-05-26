"""Hydrodynamic added mass computation."""

import numpy as np


class AddedMass:
    """Added mass from potential flow theory."""
    
    def __init__(self, rho: float = 1025.0):
        self.rho = rho
        
    def circular_cylinder(self, D: float, L: float) -> float:
        """Added mass for circular cylinder: M_a = ρ·π·D²/4·L"""
        A = np.pi * D**2 / 4
        return self.rho * A * L
    
    def square_cylinder(self, B: float, L: float) -> float:
        """Added mass for square cylinder."""
        A = B**2
        return self.rho * A * L * 1.5
    
    def heave_plate(self, A: float) -> float:
        """Added mass for heave plate."""
        return self.rho * A**1.5
    
    def frequency_dependent(self, omega: float, D: float, L: float) -> float:
        """Frequency-dependent added mass."""
        M_a_inf = self.circular_cylinder(D, L)
        # Simplified frequency dependence
        return M_a_inf * (1 - np.exp(-0.1 * omega))
    
    def added_mass_coefficient(self, D: float, L: float) -> float:
        """Added mass coefficient C_a = M_a / (ρ·π·D²/4·L)"""
        M_a = self.circular_cylinder(D, L)
        A = np.pi * D**2 / 4
        return M_a / (self.rho * A * L)
