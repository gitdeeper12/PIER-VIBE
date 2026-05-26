"""Canonical parameter registry for PIER-VIBE v1.0.0."""

from dataclasses import dataclass


@dataclass
class BenchmarkParameters:
    """Canonical parameters from paper validation."""
    
    # Safety thresholds
    BSHI_MIN: float = 0.85
    BSHI_WARNING: float = 0.75
    BSHI_CRITICAL: float = 0.65
    
    # Scour parameters
    D_S_CRIT: float = 4.2
    C_S: float = 0.025
    
    # Fatigue parameters
    D_FAT_CRIT: float = 0.80
    DETAIL_CATEGORY: str = "B"
    
    # Resonance parameters
    FREQ_DRIFT_CRIT: float = 5.0
    
    # BSHI weights
    W_SCOUR: float = 0.35
    W_FATIGUE: float = 0.35
    W_RESONANCE: float = 0.30
    
    # AI performance (from Table 2)
    PINN_SCOUR_RMSE: float = 0.075
    PINN_FATIGUE_MAE: float = 0.028
    BSHI_PRECISION: float = 0.97
    BSHI_RECALL: float = 0.95
    FALSE_ALERT_RATE: float = 0.028
    
    # Validation results (from Table 1)
    MEAN_BSHI_ACCURACY: float = 0.969
    MEAN_SCOUR_RMSE: float = 0.075
    MEAN_FATIGUE_MAE: float = 0.028
    RESONANCE_SENSITIVITY: float = 0.944


BENCHMARK_PARAMS = BenchmarkParameters()
