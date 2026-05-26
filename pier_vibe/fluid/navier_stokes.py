"""Incompressible Navier-Stokes solver with ALE formulation."""

import numpy as np


class NavierStokesSolver:
    """Navier-Stokes equations solver for fluid domain."""
    
    def __init__(self, rho: float = 1025.0, mu: float = 1.0e-3):
        self.rho = rho  # kg/m³
        self.mu = mu    # Pa·s
        
    def continuity(self, v: np.ndarray) -> np.ndarray:
        """∇·v = 0 (mass conservation)"""
        return np.gradient(v).sum()
    
    def momentum(self, v: np.ndarray, p: np.ndarray, 
                 dt: float, f_FSI: np.ndarray = None) -> np.ndarray:
        """ρ[∂v/∂t + (v·∇)v] = -∇p + μ∇²v + ρg + f_FSI"""
        grad_v = np.gradient(v)
        conv = np.dot(v, grad_v)
        lap = np.gradient(np.gradient(v))
        
        dv_dt = -np.gradient(p) / self.rho + self.mu / self.rho * lap - conv + 9.81
        
        if f_FSI is not None:
            dv_dt += f_FSI / self.rho
            
        return v + dt * dv_dt
    
    def solve(self, v0: np.ndarray, p0: np.ndarray, 
              dt: float, n_steps: int = 100) -> np.ndarray:
        """Time-marching NS solver."""
        v = v0.copy()
        for _ in range(n_steps):
            v = self.momentum(v, p0, dt)
        return v
