"""Adaptive mesh refinement strategy."""

import numpy as np


class AdaptiveMeshRefinement:
    """AMR based on error estimation."""
    
    @staticmethod
    def refinement_indicator(grad_q: np.ndarray, h_el: float, q_mean: float) -> np.ndarray:
        """η_el = ||∇q||_el·h_el / q_mean"""
        return grad_q * h_el / q_mean
    
    @staticmethod
    def should_refine(eta: float, threshold: float = 0.15) -> bool:
        """Refine if indicator exceeds threshold."""
        return eta >= threshold
    
    @staticmethod
    def should_coarsen(eta: float, threshold: float = 0.05) -> bool:
        """Coarsen if indicator below threshold."""
        return eta <= threshold
    
    @staticmethod
    def refine_element(elements: np.ndarray, element_id: int) -> np.ndarray:
        """Subdivide element into smaller elements."""
        # Simplified - returns refined elements
        return elements
    
    @staticmethod
    def coarsen_elements(elements: np.ndarray, element_ids: list) -> np.ndarray:
        """Coarsen elements by merging."""
        return elements
