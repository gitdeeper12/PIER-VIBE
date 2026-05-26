"""Goodman mean stress correction for fatigue analysis."""

import numpy as np


class GoodmanCorrection:
    """Goodman diagram mean stress correction."""
    
    def __init__(self, sigma_UTS: float = 500.0):
        self.sigma_UTS = sigma_UTS  # Ultimate tensile strength (MPa)
        
    def correct(self, sigma_a: float, sigma_m: float) -> float:
        """σ_a,eq = σ_a / (1 - σ_m/σ_UTS)"""
        if sigma_m >= self.sigma_UTS:
            return float('inf')
        return sigma_a / (1 - sigma_m / self.sigma_UTS)
    
    def equivalent_amplitude(self, sigma_max: float, sigma_min: float) -> tuple:
        """Compute amplitude and mean from max/min."""
        sigma_a = (sigma_max - sigma_min) / 2
        sigma_m = (sigma_max + sigma_min) / 2
        return sigma_a, sigma_m
    
    def allowable_amplitude(self, sigma_m: float) -> float:
        """Allowable stress amplitude at given mean stress."""
        return self.sigma_UTS * (1 - sigma_m / self.sigma_UTS)
    
    def safety_factor(self, sigma_a: float, sigma_m: float) -> float:
        """Fatigue safety factor based on Goodman criterion."""
        sigma_a_eq = self.correct(sigma_a, sigma_m)
        return self.sigma_UTS / sigma_a_eq if sigma_a_eq > 0 else float('inf')
