"""Kalman filter implementation for state estimation."""

import numpy as np


class KalmanFilter:
    """Standard Kalman filter for linear systems."""
    
    def __init__(self, n_states: int, n_measurements: int):
        self.n = n_states
        self.m = n_measurements
        
        # State vector
        self.x = np.zeros(n_states)
        
        # State covariance
        self.P = np.eye(n_states)
        
        # Process noise covariance
        self.Q = np.eye(n_states) * 0.01
        
        # Measurement noise covariance
        self.R = np.eye(n_measurements) * 0.1
        
        # State transition matrix
        self.F = np.eye(n_states)
        
        # Measurement matrix
        self.H = np.zeros((n_measurements, n_states))
        
    def predict(self, dt: float = 1.0) -> np.ndarray:
        """Prediction step: x̂(t|t-1) = F·x̂(t-1|t-1)"""
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q
        return self.x
    
    def update(self, z: np.ndarray) -> np.ndarray:
        """Update step: x̂(t|t) = x̂(t|t-1) + K·[z - H·x̂(t|t-1)]"""
        # Innovation
        y = z - self.H @ self.x
        
        # Innovation covariance
        S = self.H @ self.P @ self.H.T + self.R
        
        # Kalman gain
        K = self.P @ self.H.T @ np.linalg.inv(S)
        
        # State update
        self.x = self.x + K @ y
        
        # Covariance update
        I = np.eye(self.n)
        self.P = (I - K @ self.H) @ self.P
        
        return self.x
    
    def set_initial_state(self, x0: np.ndarray):
        """Set initial state estimate."""
        self.x = x0.copy()
    
    def get_state(self) -> np.ndarray:
        """Get current state estimate."""
        return self.x
    
    def get_covariance(self) -> np.ndarray:
        """Get state covariance matrix."""
        return self.P
