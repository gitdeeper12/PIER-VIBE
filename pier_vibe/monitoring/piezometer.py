"""Piezometer sensor handler for pore pressure monitoring."""

import numpy as np
from datetime import datetime


class Piezometer:
    """Piezometer for foundation pore pressure."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.readings = []
        
    def read(self) -> dict:
        """Simulate piezometer reading."""
        pressure = 100 + np.random.randn() * 10  # kPa
        return {
            "timestamp": datetime.now().isoformat(),
            "pressure_kPa": pressure,
            "head_m": pressure / 9.81,
            "sensor_id": self.sensor_id
        }
    
    def compute_head(self, pressure_kPa: float) -> float:
        """h = p/γ_w (meters of water head)"""
        return pressure_kPa / 9.81
    
    def detect_anomaly(self, threshold_kPa: float = 150) -> bool:
        """Detect pore pressure anomaly."""
        reading = self.read()
        return reading["pressure_kPa"] > threshold_kPa
