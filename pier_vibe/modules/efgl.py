"""EFGL: Elastic Fatigue Governance Lock - Module 03.

Implements Palmgren-Miner fatigue accumulation.
"""

import numpy as np


class EFGL:
    """Elastic Fatigue Governance Lock."""
    
    def __init__(self, detail_category: str = "B"):
        self.detail_category = detail_category
        self.S_N_params = self._get_sn_params(detail_category)
        
    def _get_sn_params(self, category: str) -> dict:
        """S-N curve parameters for detail category."""
        params = {
            "B": {"C": 3.5e12, "m": 3.0, "Δσ_c": 125},
            "C": {"C": 1.8e12, "m": 3.0, "Δσ_c": 100},
            "D": {"C": 8.8e11, "m": 3.0, "Δσ_c": 80},
            "E": {"C": 3.9e11, "m": 3.0, "Δσ_c": 70},
        }
        return params.get(category, params["B"])
    
    def compute_cycles_to_failure(self, stress_amplitude_MPa: float) -> float:
        """Number of cycles to failure N_i(σ_a) from S-N curve."""
        C = self.S_N_params["C"]
        m = self.S_N_params["m"]
        return C / stress_amplitude_MPa**m
    
    def compute_fatigue_damage(self, cycles: list, stress_amplitudes: list) -> float:
        """Palmgren-Miner cumulative damage D = Σ n_i / N_i."""
        damage = 0.0
        for n_i, sigma_a in zip(cycles, stress_amplitudes):
            N_i = self.compute_cycles_to_failure(sigma_a)
            damage += n_i / N_i
        return min(damage, 1.0)
    
    def goodman_correction(self, sigma_a: float, sigma_m: float, 
                           sigma_UTS: float = 500) -> float:
        """Goodman mean stress correction.
        
        σ_a,eq = σ_a / (1 - σ_m/σ_UTS)
        """
        return sigma_a / (1 - sigma_m / sigma_UTS)
    
    def rainflow_counting(self, stress_history: list) -> tuple:
        """Simplified rainflow cycle counting."""
        # Simplified implementation
        half_cycles = []
        for i in range(1, len(stress_history)):
            half_cycles.append(abs(stress_history[i] - stress_history[i-1]))
        return half_cycles, [1] * len(half_cycles)
