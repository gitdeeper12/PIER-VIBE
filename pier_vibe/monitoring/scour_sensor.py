"""Scour sensor handler (sonar/magnetic resonance/TDR)."""

import numpy as np
from datetime import datetime


class ScourSensor:
    """Scour depth monitoring sensor."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.readings = []
        self.baseline_depth = 0.0
        
    def read(self) -> dict:
        """Simulate scour sensor reading."""
        depth = self.baseline_depth + np.random.randn() * 0.05
        return {
            "timestamp": datetime.now().isoformat(),
            "scour_depth_m": max(0, depth),
            "sensor_id": self.sensor_id
        }
    
    def set_baseline(self, depth_m: float):
        """Set baseline (pre-scour) depth."""
        self.baseline_depth = depth_m
    
    def get_scour_rate(self, hours: int = 24) -> float:
        """Compute scour rate over period (m/hour)."""
        if len(self.readings) < 2:
            return 0.0
        delta_depth = self.readings[-1]["scour_depth_m"] - self.readings[0]["scour_depth_m"]
        return delta_depth / hours
    
    def is_critical(self, critical_depth: float = 4.2) -> bool:
        """Check if scour depth exceeds critical threshold."""
        reading = self.read()
        return reading["scour_depth_m"] > critical_depth
