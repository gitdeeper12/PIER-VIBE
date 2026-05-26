"""Morison equation wave forces on bridge piers."""

import numpy as np


class WaveForces:
    """Morison equation for wave-induced forces."""
    
    def __init__(self, rho: float = 1025.0, C_m: float = 2.0, C_d: float = 1.0):
        self.rho = rho
        self.C_m = C_m  # Inertia coefficient
        self.C_d = C_d  # Drag coefficient
        
    def inertia_force(self, D: float, du_dt: float) -> float:
        """F_i = ρ·C_m·(πD²/4)·du/dt"""
        A = np.pi * D**2 / 4
        return self.rho * self.C_m * A * du_dt
    
    def drag_force(self, D: float, u: float) -> float:
        """F_d = ½ρ·C_d·D·u·|u|"""
        return 0.5 * self.rho * self.C_d * D * u * abs(u)
    
    def total_force(self, D: float, u: float, du_dt: float) -> float:
        """F = F_i + F_d"""
        return self.inertia_force(D, du_dt) + self.drag_force(D, u)
    
    def wave_velocity(self, H: float, T: float, z: float, d: float) -> float:
        """Linear wave theory velocity at depth z."""
        k = 2 * np.pi / (1.56 * T**2)  # Deep water approximation
        omega = 2 * np.pi / T
        return H * omega * np.cosh(k * (z + d)) / np.sinh(k * d) / 2
