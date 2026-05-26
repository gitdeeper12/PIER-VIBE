"""Meteorological and oceanographic sensor handler."""

import numpy as np
from datetime import datetime


class MeteorologicalSensor:
    """Wind, wave, and current monitoring."""
    
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        
    def read_wind(self) -> dict:
        """Wind speed and direction."""
        return {
            "timestamp": datetime.now().isoformat(),
            "speed_mps": 5 + np.random.randn() * 2,
            "direction_deg": np.random.uniform(0, 360),
            "gust_mps": 7 + np.random.randn() * 3,
            "sensor_id": self.sensor_id
        }
    
    def read_wave(self) -> dict:
        """Wave height, period, direction."""
        return {
            "timestamp": datetime.now().isoformat(),
            "significant_height_m": 1.5 + np.random.randn() * 0.5,
            "peak_period_s": 6 + np.random.randn(),
            "direction_deg": np.random.uniform(0, 360),
            "sensor_id": self.sensor_id
        }
    
    def read_current(self) -> dict:
        """Current velocity profile."""
        return {
            "timestamp": datetime.now().isoformat(),
            "surface_mps": 1.2 + np.random.randn() * 0.3,
            "mid_depth_mps": 0.8 + np.random.randn() * 0.2,
            "bottom_mps": 0.4 + np.random.randn() * 0.1,
            "direction_deg": np.random.uniform(0, 360),
            "sensor_id": self.sensor_id
        }
    
    def read_water_level(self) -> dict:
        """Water level (tide)."""
        return {
            "timestamp": datetime.now().isoformat(),
            "level_m": 2.5 + np.sin(datetime.now().timestamp() / 3600) * 1.5,
            "sensor_id": self.sensor_id
        }
