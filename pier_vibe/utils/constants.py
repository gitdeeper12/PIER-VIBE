"""Canonical parameter registry for PIER-VIBE v1.0.0."""

from dataclasses import dataclass


@dataclass
class BridgeConstants:
    """Canonical parameters from paper validation."""
    
    # Safety thresholds
    BSHI_MIN: float = 0.85
    BSHI_WARNING: float = 0.75
    BSHI_CRITICAL: float = 0.65
    
    # Scour parameters
    D_S_CRIT: float = 4.2  # Critical scour depth (m)
    C_S: float = 0.025  # Scour rate coefficient
    D50_REF: float = 0.5  # Reference grain size (mm)
    
    # Fatigue parameters
    D_FAT_CRIT: float = 0.80  # Critical fatigue damage
    DETAIL_CATEGORY: str = "B"
    SIGMA_UTS: float = 500.0  # Ultimate tensile strength (MPa)
    
    # Resonance parameters
    FREQ_DRIFT_CRIT: float = 5.0  # Critical frequency drift (%)
    SAFE_SEPARATION: float = 0.05  # Minimum safe frequency separation
    
    # Weights for BSHI
    W_SCOUR: float = 0.35
    W_FATIGUE: float = 0.35
    W_RESONANCE: float = 0.30
    
    # Environmental constants
    RHO_WATER: float = 1025.0  # kg/m³ (seawater)
    G: float = 9.81  # m/s²
    GAMMA_W: float = 9.81  # kN/m³
    
    # Numerical parameters
    MESH_SIZE: int = 100000
    
    # AI performance (from Table 2)
    PINN_SCOUR_RMSE: float = 0.075  # m
    PINN_FATIGUE_MAE: float = 0.028  # 2.8%
    BSHI_PRECISION: float = 0.97
    BSHI_RECALL: float = 0.95
    FALSE_ALERT_RATE: float = 0.028
    
    # Validation results (from Table 1)
    MEAN_BSHI_ACCURACY: float = 0.969
    MEAN_SCOUR_RMSE: float = 0.075
    MEAN_FATIGUE_MAE: float = 0.028
    RESONANCE_SENSITIVITY: float = 0.944


CONSTANTS = BridgeConstants()
