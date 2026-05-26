"""Measurement model for Kalman filter."""

import numpy as np


class MeasurementModel:
    """Linear measurement model z = H·x + v."""
    
    def __init__(self, n_states: int, n_measurements: int):
        self.n = n_states
        self.m = n_measurements
        self.H = np.zeros((n_measurements, n_states))
        
    def set_measurement_matrix(self, H: np.ndarray):
        """Set measurement matrix."""
        self.H = H
    
    def predict_measurement(self, x: np.ndarray) -> np.ndarray:
        """ẑ = H·x"""
        return self.H @ x
    
    def compute_innovation(self, z: np.ndarray, x: np.ndarray) -> np.ndarray:
        """y = z - H·x"""
        return z - self.predict_measurement(x)
    
    def identity_measurement(self, idx: int) -> None:
        """Set measurement matrix to identity for a state."""
        self.H[idx, idx] = 1.0
    
    def custom_measurement(self, mapping: dict):
        """Custom measurement mapping."""
        for meas_idx, state_idx in mapping.items():
            self.H[meas_idx, state_idx] = 1.0
