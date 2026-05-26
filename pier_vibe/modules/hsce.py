"""HSCE: Hydro-Structural Coupling Evaluator - Module 02.

Implements fluid-structure-soil coupling for bridge piers.
"""

import numpy as np


class HSCE:
    """Hydro-Structural Coupling Evaluator."""
    
    def __init__(self, pier_diameter: float = 3.5, water_depth: float = 25.0):
        self.D_pier = pier_diameter
        self.y = water_depth
        self.rho_F = 1025.0  # kg/m³ (seawater)
        
    def compute_morison_force(self, u: float, du_dt: float, 
                              C_m: float = 2.0, C_d: float = 1.0) -> float:
        """Morison equation wave force.
        
        F = ρ_F·C_m·(πD²/4)·du/dt + ½ρ_F·C_d·D·u|u|
        """
        A = np.pi * self.D_pier**2 / 4  # Cross-sectional area
        
        inertia = self.rho_F * C_m * A * du_dt
        drag = 0.5 * self.rho_F * C_d * self.D_pier * u * abs(u)
        
        return inertia + drag
    
    def compute_added_mass(self, L_sub: float = 20.0) -> float:
        """Hydrodynamic added mass M_a.
        
        M_a = ρ_F · π · D²/4 · L_sub
        """
        A = np.pi * self.D_pier**2 / 4
        return self.rho_F * A * L_sub
    
    def compute_froude_number(self, u: float) -> float:
        """Froude number Fr = u / sqrt(g·y)."""
        return u / np.sqrt(9.81 * self.y)
    
    def compute_wave_number(self, T: float) -> float:
        """Dispersion relation for wave number k."""
        omega = 2 * np.pi / T
        # Simplified deep water approximation
        return omega**2 / 9.81
