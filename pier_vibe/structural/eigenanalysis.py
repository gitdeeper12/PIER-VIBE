"""Eigenfrequency and mode shape analysis."""

import numpy as np


class Eigenanalysis:
    """Structural eigenvalue analysis."""
    
    def __init__(self, stiffness_matrix: np.ndarray = None, 
                 mass_matrix: np.ndarray = None):
        self.K = stiffness_matrix
        self.M = mass_matrix
        
    def natural_frequencies(self) -> np.ndarray:
        """Compute natural frequencies ω_i from K·φ = ω²·M·φ"""
        if self.K is None or self.M is None:
            # Return synthetic frequencies for demonstration
            return np.array([0.85, 1.23, 2.45])  # Hz
        
        # Solve generalized eigenvalue problem
        eigvals = np.linalg.eigvals(np.linalg.solve(self.M, self.K))
        omega = np.sqrt(np.abs(eigvals))
        return omega / (2 * np.pi)  # Convert to Hz
    
    def mode_shapes(self, n_modes: int = 3) -> np.ndarray:
        """Extract first n mode shapes φ_i."""
        if self.K is None or self.M is None:
            return np.random.rand(n_modes, 10)  # Synthetic
        eigvecs = np.linalg.eig(np.linalg.solve(self.M, self.K))[1]
        return eigvecs[:, :n_modes]
    
    def participation_factor(self, mode_shape: np.ndarray, 
                             excitation: np.ndarray) -> float:
        """Modal participation factor Γ_i = φ_iᵀ·F / (φ_iᵀ·M·φ_i)"""
        if self.M is None:
            return np.dot(mode_shape, excitation)
        return np.dot(mode_shape, excitation) / np.dot(mode_shape, np.dot(self.M, mode_shape))
