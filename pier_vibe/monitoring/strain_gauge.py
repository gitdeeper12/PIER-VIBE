"""Vibrating-wire strain gauge sensor handler."""

import numpy as np
from datetime import datetime


class StrainGauge:
    """Strain gauge for structural stress monitoring."""
    
    def __init__(self, sensor_id: str, E: float = 200e9):
        self.sensor_id = sensor_id
        self.E = E  # Young's modulus (Pa)
        self.readings = []
        
    def read(self) -> dict:
        """Simulate strain gauge reading."""
        strain = np.random.randn() * 50e-6  # microstrain
        return {
            "timestamp": datetime.now().isoformat(),
            "strain_ue": strain * 1e6,
            "stress_MPa": strain * self.E / 1e6,
            "sensor_id": self.sensor_id
        }
    
    def compute_stress(self, strain_ue: float) -> float:
        """σ = E·ε"""
        return strain_ue * 1e-6 * self.E / 1e6  # MPa
    
    def detect_crack(self, threshold_ue: float = 500) -> bool:
        """Detect possible crack from strain spike."""
        reading = self.read()
        return abs(reading["strain_ue"]) > threshold_ue
