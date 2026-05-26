"""Structural damping matrix computation."""

import numpy as np


class DampingCalculator:
    """Rayleigh damping and modal damping."""
    
    def __init__(self, mass_matrix: np.ndarray = None, 
                 stiffness_matrix: np.ndarray = None):
        self.M = mass_matrix
        self.K = stiffness_matrix
        
    def rayleigh_damping(self, alpha: float = 0.05, beta: float = 0.002) -> np.ndarray:
        """Rayleigh damping C = α·M + β·K"""
        if self.M is None or self.K is None:
            return np.eye(10) * 0.05  # Synthetic
        return alpha * self.M + beta * self.K
    
    def modal_damping_ratio(self, omega: float, alpha: float = 0.05, 
                            beta: float = 0.002) -> float:
        """Modal damping ratio ζ = (α/2ω + βω/2)"""
        return alpha / (2 * omega) + beta * omega / 2
    
    def critical_damping(self, omega: float) -> float:
        """Critical damping C_crit = 2·M·ω"""
        if self.M is None:
            return 2 * omega
        return 2 * np.max(np.linalg.eigvals(self.M)) * omega
    
    def added_damping(self, rho: float = 1025.0, A: float = 10.0, 
                      C_a: float = 0.5) -> float:
        """Hydrodynamic added damping C_a = ρ·C_a·A·v"""
        return rho * C_a * A
