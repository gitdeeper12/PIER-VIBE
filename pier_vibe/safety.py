"""Safety certification and decision logic for PIER-VIBE."""

from dataclasses import dataclass
from enum import Enum


class SafetySignal(Enum):
    STABILITY_CERTIFIED = "🟢 STABILITY CERTIFIED"
    MONITORING_PHASE = "🟠 MONITORING PHASE"
    STOP_COMMAND = "🔴 STOP COMMAND"


@dataclass
class SafetyCertifier:
    """Certifies bridge safety based on BSHI thresholds."""
    
    BSHI_MIN = 0.85
    BSHI_WARNING = 0.75
    BSHI_CRITICAL = 0.65
    D_S_CRIT = 4.2
    D_FAT_CRIT = 0.80
    FREQ_DRIFT_CRIT = 5.0
    
    @classmethod
    def compute_bshi(cls, scour_depth: float, fatigue_damage: float, 
                     freq_drift_pct: float) -> float:
        """Bridge Structural Health Index."""
        w_s, w_f, w_r = 0.35, 0.35, 0.30
        s_term = w_s * (1 - min(scour_depth / cls.D_S_CRIT, 1.0))
        f_term = w_f * (1 - min(fatigue_damage / cls.D_FAT_CRIT, 1.0))
        r_term = w_r * (1 - min(freq_drift_pct / cls.FREQ_DRIFT_CRIT, 1.0))
        return s_term + f_term + r_term
    
    @classmethod
    def classify(cls, bshi: float) -> tuple:
        """Classify safety status based on BSHI thresholds."""
        if bshi >= cls.BSHI_MIN:
            return True, SafetySignal.STABILITY_CERTIFIED, "Normal operation"
        elif bshi >= cls.BSHI_WARNING:
            return True, SafetySignal.MONITORING_PHASE, "Reduced operations"
        elif bshi >= cls.BSHI_CRITICAL:
            return False, SafetySignal.MONITORING_PHASE, "Load restriction"
        else:
            return False, SafetySignal.STOP_COMMAND, "Bridge closure"
