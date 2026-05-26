"""Palmgren-Miner linear cumulative damage rule."""

import numpy as np


class PalmgrenMiner:
    """Linear cumulative fatigue damage D = Σ n_i/N_i."""
    
    def __init__(self):
        self.D = 0.0  # Cumulative damage
        
    def add_cycles(self, n_i: float, N_i: float) -> float:
        """Add cycles to cumulative damage."""
        self.D += n_i / N_i
        return self.D
    
    def reset(self):
        """Reset cumulative damage."""
        self.D = 0.0
    
    def is_failed(self) -> bool:
        """Check if fatigue failure has occurred (D ≥ 1.0)."""
        return self.D >= 1.0
    
    def remaining_life(self, current_damage: float, 
                       damage_rate_per_year: float) -> float:
        """Estimate remaining service life in years."""
        if damage_rate_per_year <= 0:
            return float('inf')
        return (1.0 - current_damage) / damage_rate_per_year
    
    def damage_rate(self, cycles_per_year: float, N_f: float) -> float:
        """Annual damage accumulation rate."""
        return cycles_per_year / N_f
