"""Nonlinear FEM solver (Newton-Raphson)."""

import numpy as np


class NonLinearSolver:
    """Newton-Raphson iterative solver for nonlinear problems."""
    
    @staticmethod
    def solve(K: np.ndarray, F: np.ndarray, u0: np.ndarray, 
              max_iter: int = 100, tol: float = 1e-6) -> np.ndarray:
        """Solve K·u = F using Newton-Raphson."""
        u = u0.copy()
        for i in range(max_iter):
            residual = F - K @ u
            if np.linalg.norm(residual) < tol:
                break
            du = np.linalg.solve(K, residual)
            u += du
        return u
    
    @staticmethod
    def modified_newton(K: np.ndarray, F: np.ndarray, u0: np.ndarray,
                        max_iter: int = 100, tol: float = 1e-6) -> np.ndarray:
        """Modified Newton method with constant stiffness matrix."""
        u = u0.copy()
        for i in range(max_iter):
            residual = F - K @ u
            if np.linalg.norm(residual) < tol:
                break
            du = np.linalg.solve(K, residual)
            u += du
        return u
    
    @staticmethod
    def line_search(u: np.ndarray, du: np.ndarray, residual: np.ndarray,
                    alpha_max: float = 1.0) -> float:
        """Line search for optimal step size."""
        # Simplified - return alpha = 1.0
        return 1.0
