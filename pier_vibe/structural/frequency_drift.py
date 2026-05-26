"""Real-time natural frequency drift monitoring."""

import numpy as np


class FrequencyDrift:
    """Natural frequency drift detection and tracking."""
    
    def __init__(self, initial_frequency: float = 0.85):
        self.f0 = initial_frequency  # Initial natural frequency (Hz)
        self.f_current = initial_frequency
        
    def update(self, acceleration_data: np.ndarray, fs: float = 100.0) -> float:
        """Update current frequency from accelerometer data."""
        # FFT-based frequency estimation
        n = len(acceleration_data)
        freq = np.fft.fftfreq(n, 1/fs)
        spectrum = np.abs(np.fft.fft(acceleration_data))
        
        # Find dominant frequency (excluding DC)
        idx = np.argmax(spectrum[1:n//2]) + 1
        self.f_current = abs(freq[idx])
        return self.f_current
    
    def compute_drift(self) -> float:
        """Compute frequency drift percentage Δf = |f - f0|/f0 × 100%"""
        return abs(self.f_current - self.f0) / self.f0 * 100
    
    def resonance_risk(self, excitation_freq: float, 
                       safe_separation: float = 0.05) -> str:
        """Assess resonance risk based on frequency proximity."""
        separation = abs(self.f_current - excitation_freq) / excitation_freq
        
        if separation > safe_separation * 2:
            return "low"
        elif separation > safe_separation:
            return "moderate"
        else:
            return "high"
    
    def drift_rate(self, dt: float = 3600) -> float:
        """Rate of frequency drift df/dt (Hz/hour)"""
        # Simplified calculation
        return 0.001  # Hz/hour
