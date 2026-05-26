"""Tri-axial accelerometer sensor handler."""

import numpy as np
from datetime import datetime


class Accelerometer:
    """Tri-axial accelerometer for structural vibration monitoring."""
    
    SAMPLING_RATE = 100  # Hz
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.readings = []
        
    def read(self) -> dict:
        """Simulate accelerometer reading."""
        return {
            "timestamp": datetime.now().isoformat(),
            "ax": np.random.randn() * 0.05,
            "ay": np.random.randn() * 0.05,
            "az": np.random.randn() * 0.05 + 9.81,
            "sensor_id": self.sensor_id
        }
    
    def get_fft(self, n_samples: int = 1024) -> tuple:
        """Compute FFT of acceleration signal."""
        data = np.random.randn(n_samples)
        freq = np.fft.fftfreq(n_samples, 1/self.SAMPLING_RATE)
        spectrum = np.abs(np.fft.fft(data))
        return freq[:n_samples//2], spectrum[:n_samples//2]
    
    def detect_impact(self, threshold: float = 2.0) -> bool:
        """Detect impact event from acceleration."""
        reading = self.read()
        acc_magnitude = np.sqrt(reading["ax"]**2 + reading["ay"]**2 + reading["az"]**2)
        return acc_magnitude > threshold
