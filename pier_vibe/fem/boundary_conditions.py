"""Boundary conditions for bridge pier analysis."""

import numpy as np


class BoundaryConditions:
    """Apply BCs for fluid, structure, and soil domains."""
    
    @staticmethod
    def velocity_inlet(u_in: float, v_in: float = 0, w_in: float = 0) -> dict:
        """Velocity inlet boundary condition."""
        return {"type": "inlet", "velocity": [u_in, v_in, w_in]}
    
    @staticmethod
    def pressure_outlet(p_out: float = 0) -> dict:
        """Pressure outlet boundary condition."""
        return {"type": "outlet", "pressure": p_out}
    
    @staticmethod
    def wall_no_slip() -> dict:
        """No-slip wall boundary condition."""
        return {"type": "wall", "slip": "no"}
    
    @staticmethod
    def free_surface() -> dict:
        """Free surface boundary condition."""
        return {"type": "free_surface", "pressure": 0}
    
    @staticmethod
    def fixed_displacement(u: float = 0, v: float = 0, w: float = 0) -> dict:
        """Fixed displacement boundary condition."""
        return {"type": "fixed", "displacement": [u, v, w]}
    
    @staticmethod
    def spring_boundary(k: float) -> dict:
        """Spring boundary condition (soil-structure interface)."""
        return {"type": "spring", "stiffness": k}
