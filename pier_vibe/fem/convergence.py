"""Convergence criteria and numerical stability."""

import numpy as np


class ConvergenceChecker:
    """Check solution convergence."""
    
    @staticmethod
    def displacement_convergence(u_new: np.ndarray, u_old: np.ndarray, 
                                  tol: float = 1e-6) -> bool:
        """Check displacement convergence."""
        diff = np.linalg.norm(u_new - u_old)
        return diff < tol
    
    @staticmethod
    def residual_convergence(residual: np.ndarray, tol: float = 1e-5) -> bool:
        """Check residual convergence."""
        return np.linalg.norm(residual) < tol
    
    @staticmethod
    def energy_convergence(u_new: np.ndarray, u_old: np.ndarray, 
                           residual: np.ndarray, tol: float = 1e-8) -> bool:
        """Check energy convergence (du·R < tol)."""
        du = u_new - u_old
        return abs(np.dot(du, residual)) < tol
    
    @staticmethod
    def relative_convergence(u_new: np.ndarray, u_old: np.ndarray, 
                             tol: float = 1e-3) -> bool:
        """Check relative convergence."""
        norm_u = np.linalg.norm(u_new)
        if norm_u < 1e-12:
            return True
        return np.linalg.norm(u_new - u_old) / norm_u < tol
