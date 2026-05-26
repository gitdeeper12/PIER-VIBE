"""Finite element discretization module.

Components:
- Adaptive mesh generation
- Adaptive mesh refinement (AMR)
- Boundary conditions
- Nonlinear solver
- Convergence criteria
"""

from .mesh import MeshGenerator
from .amr import AdaptiveMeshRefinement
from .boundary_conditions import BoundaryConditions
from .solver import NonLinearSolver
from .convergence import ConvergenceChecker

__all__ = ["MeshGenerator", "AdaptiveMeshRefinement", "BoundaryConditions", "NonLinearSolver", "ConvergenceChecker"]
