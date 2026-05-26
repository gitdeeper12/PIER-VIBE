"""Mode shape extraction and analysis."""

import numpy as np


class ModeShapes:
    """Mode shape extraction utilities."""
    
    @staticmethod
    def normalize(phi: np.ndarray, mass_matrix: np.ndarray = None) -> np.ndarray:
        """Normalize mode shape to unit modal mass."""
        if mass_matrix is None:
            return phi / np.linalg.norm(phi)
        modal_mass = np.dot(phi, np.dot(mass_matrix, phi))
        return phi / np.sqrt(modal_mass)
    
    @staticmethod
    def orthogonality(phi_i: np.ndarray, phi_j: np.ndarray, 
                      mass_matrix: np.ndarray = None) -> float:
        """Check orthogonality φ_iᵀ·M·φ_j."""
        if mass_matrix is None:
            return np.dot(phi_i, phi_j)
        return np.dot(phi_i, np.dot(mass_matrix, phi_j))
    
    @staticmethod
    def mac(phi_i: np.ndarray, phi_j: np.ndarray) -> float:
        """Modal Assurance Criterion (MAC)."""
        numerator = np.dot(phi_i, phi_j)**2
        denominator = np.dot(phi_i, phi_i) * np.dot(phi_j, phi_j)
        return numerator / denominator if denominator > 0 else 0
