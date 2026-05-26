"""S-N curves for structural detail categories."""

import numpy as np


class SNCurves:
    """S-N curves according to detail category."""
    
    # S-N curve parameters: N = C·Δσ^(-m)
    DETAIL_CATEGORIES = {
        "A": {"C": 5.0e12, "m": 3.0, "Δσ_c": 180},
        "B": {"C": 3.5e12, "m": 3.0, "Δσ_c": 125},
        "C": {"C": 1.8e12, "m": 3.0, "Δσ_c": 100},
        "D": {"C": 8.8e11, "m": 3.0, "Δσ_c": 80},
        "E": {"C": 3.9e11, "m": 3.0, "Δσ_c": 70},
    }
    
    def __init__(self, category: str = "B"):
        self.category = category
        self.params = self.DETAIL_CATEGORIES.get(category, self.DETAIL_CATEGORIES["B"])
    
    def cycles_to_failure(self, delta_sigma: float) -> float:
        """N = C·Δσ^(-m)"""
        return self.params["C"] * delta_sigma**(-self.params["m"])
    
    def fatigue_limit(self) -> float:
        """Constant amplitude fatigue limit Δσ_L."""
        return self.params["Δσ_c"] * 0.5
    
    def cut_off_limit(self) -> float:
        """Cut-off limit for infinite life."""
        return self.params["Δσ_c"] * 0.2
    
    def slope_change(self) -> float:
        """Slope change for high-cycle fatigue (m₂ = 5)."""
        return 5.0
    
    def damage_at_stress(self, delta_sigma: float, n_cycles: float) -> float:
        """Damage contribution from stress range."""
        N_f = self.cycles_to_failure(delta_sigma)
        return n_cycles / N_f if N_f > 0 else 0
