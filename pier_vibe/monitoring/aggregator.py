"""Multi-sensor data aggregation and fusion."""

import numpy as np
from datetime import datetime, timedelta


class SensorAggregator:
    """Aggregate data from all monitoring systems."""
    
    def __init__(self):
        self.accelerometer = None
        self.strain_gauge = None
        self.piezometer = None
        self.scour_sensor = None
        self.meteorological = None
        
    def aggregate_all(self) -> dict:
        """Aggregate data from all sensors."""
        return {
            "accelerometer": self._get_accelerometer_data() if self.accelerometer else None,
            "strain": self._get_strain_data() if self.strain_gauge else None,
            "pore_pressure": self._get_pore_pressure() if self.piezometer else None,
            "scour_depth": self._get_scour_depth() if self.scour_sensor else None,
            "environmental": self._get_environmental() if self.meteorological else None,
            "timestamp": datetime.now().isoformat()
        }
    
    def _get_accelerometer_data(self) -> dict:
        return {"ax": 0.02, "ay": 0.01, "az": 9.81}
    
    def _get_strain_data(self) -> dict:
        return {"strain_ue": 45.2, "stress_MPa": 9.0}
    
    def _get_pore_pressure(self) -> dict:
        return {"pressure_kPa": 105.3}
    
    def _get_scour_depth(self) -> dict:
        return {"scour_depth_m": 1.8}
    
    def _get_environmental(self) -> dict:
        return {"wind_speed_mps": 5.2, "wave_height_m": 1.6, "current_mps": 0.9}
    
    def get_state_vector(self) -> np.ndarray:
        """Get combined state vector for Kalman filter."""
        agg = self.aggregate_all()
        features = [
            agg.get("scour_depth", {}).get("scour_depth_m", 0),
            agg.get("strain", {}).get("strain_ue", 0),
            agg.get("pore_pressure", {}).get("pressure_kPa", 0),
            agg.get("environmental", {}).get("wind_speed_mps", 0),
            agg.get("environmental", {}).get("wave_height_m", 0),
        ]
        return np.array(features)
