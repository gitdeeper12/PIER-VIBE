"""Arbitrary Lagrangian-Eulerian (ALE) formulation for moving boundaries."""

import numpy as np


class ALEFormulation:
    """ALE formulation for fluid-structure interaction."""
    
    def __init__(self):
        self.mesh_velocity = None
        
    def mesh_update(self, nodes: np.ndarray, displacement: np.ndarray, dt: float) -> np.ndarray:
        """Update mesh positions based on structural displacement."""
        self.mesh_velocity = displacement / dt
        return nodes + displacement
    
    def ale_convective_term(self, fluid_velocity: np.ndarray, mesh_velocity: np.ndarray) -> np.ndarray:
        """Convective term with mesh velocity (v - v_mesh)·∇v"""
        relative_velocity = fluid_velocity - mesh_velocity
        return relative_velocity * np.gradient(fluid_velocity)
    
    def interface_velocity_match(self, v_fluid: np.ndarray, v_structure: np.ndarray) -> bool:
        """Check kinematic compatibility at interface."""
        return np.allclose(v_fluid, v_structure, rtol=1e-6)
    
    def interface_stress_balance(self, sigma_fluid: np.ndarray, sigma_structure: np.ndarray) -> bool:
        """Check dynamic equilibrium at interface."""
        return np.allclose(sigma_fluid, -sigma_structure, rtol=1e-6)
