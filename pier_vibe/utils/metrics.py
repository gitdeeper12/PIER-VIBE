"""Safety metrics computation: BSHI, scour RMSE, fatigue MAE."""

import numpy as np


class SafetyMetrics:
    """Compute bridge safety performance metrics."""
    
    @staticmethod
    def bshi(scour_depth: float, fatigue_damage: float, 
             freq_drift: float, D_s_crit: float = 4.2,
             D_fat_crit: float = 0.80, freq_crit: float = 5.0) -> float:
        """Bridge Structural Health Index."""
        w_s, w_f, w_r = 0.35, 0.35, 0.30
        s_term = w_s * (1 - min(scour_depth / D_s_crit, 1.0))
        f_term = w_f * (1 - min(fatigue_damage / D_fat_crit, 1.0))
        r_term = w_r * (1 - min(freq_drift / freq_crit, 1.0))
        return s_term + f_term + r_term
    
    @staticmethod
    def scour_rmse(predicted: np.ndarray, measured: np.ndarray) -> float:
        """Root mean square error for scour depth prediction."""
        return np.sqrt(np.mean((predicted - measured)**2))
    
    @staticmethod
    def fatigue_mae(predicted: np.ndarray, measured: np.ndarray) -> float:
        """Mean absolute error for fatigue damage prediction."""
        return np.mean(np.abs(predicted - measured))
    
    @staticmethod
    def resonance_sensitivity(tp: int, fn: int) -> float:
        """Sensitivity = TP / (TP + FN)"""
        return tp / (tp + fn) if (tp + fn) > 0 else 0
    
    @staticmethod
    def false_alert_rate(fp: int, tn: int) -> float:
        """FAR = FP / (FP + TN)"""
        return fp / (fp + tn) if (fp + tn) > 0 else 0
