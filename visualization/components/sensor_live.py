"""Live sensor reading panel for PIER-VIBE dashboard."""

import streamlit as st
import pandas as pd
from datetime import datetime


class SensorLivePanel:
    """Live sensor data display panel."""
    
    def __init__(self):
        self.sensors = {
            "Accelerometer": {"ax": 0.02, "ay": 0.01, "az": 9.81},
            "Strain Gauge": {"strain_ue": 45.2, "stress_MPa": 9.0},
            "Piezometer": {"pressure_kPa": 105.3},
            "Scour Sensor": {"depth_m": 1.8},
            "Wave Sensor": {"height_m": 1.6, "period_s": 6.0}
        }
        self.timestamp = datetime.now()
        
    def render(self):
        """Render the live sensor panel."""
        st.subheader("📡 Live Sensor Readings")
        
        # Create DataFrame
        rows = []
        for sensor, data in self.sensors.items():
            for key, value in data.items():
                rows.append({"Sensor": sensor, "Parameter": key, "Value": f"{value:.2f}"})
        
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)
        
        # Last update time
        st.caption(f"Last updated: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        
    def update_readings(self):
        """Simulate reading updates."""
        import numpy as np
        self.sensors["Scour Sensor"]["depth_m"] += np.random.randn() * 0.02
        self.sensors["Accelerometer"]["ax"] = np.random.randn() * 0.02
        self.timestamp = datetime.now()
