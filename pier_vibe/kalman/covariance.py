"""Covariance matrices for Kalman filter."""

import numpy as np


class CovarianceMatrices:
    """Process and measurement noise covariance matrices."""
    
    def __init__(self, n_states: int, n_measurements: int):
        self.n = n_states
        self.m = n_measurements
        self.Q = np.eye(n_states) * 0.01
        self.R = np.eye(n_measurements) * 0.1
        
    def set_process_noise(self, Q: np.ndarray):
        """Set process noise covariance."""
        self.Q = Q
    
    def set_measurement_noise(self, R: np.ndarray):
        """Set measurement noise covariance."""
        self.R = R
    
    def diagonal_process_noise(self, variances: np.ndarray):
        """Set diagonal process noise."""
        self.Q = np.diag(variances)
    
    def diagonal_measurement_noise(self, variances: np.ndarray):
        """Set diagonal measurement noise."""
        self.R = np.diag(variances)
    
    def scaled_identity(self, scale: float, is_process: bool = True) -> np.ndarray:
        """Return scaled identity matrix."""
        if is_process:
            return np.eye(self.n) * scale
        return np.eye(self.m) * scale
    
    def adaptive_noise(self, innovation: np.ndarray) -> None:
        """Adaptive noise estimation from innovation sequence."""
        # Simplified adaptive noise update
        S = innovation @ innovation.T
        self.R = 0.95 * self.R + 0.05 * S
