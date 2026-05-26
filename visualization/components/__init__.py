"""Dashboard UI components for PIER-VIBE.

Components:
- Signal panel: Safety status indicator (🟢🟠🔴)
- Forecast panel: PINN scour and fatigue forecasts
- Sensor live panel: Real-time sensor readings
"""

from .signal_panel import SignalPanel
from .forecast_panel import ForecastPanel
from .sensor_live import SensorLivePanel

__all__ = ["SignalPanel", "ForecastPanel", "SensorLivePanel"]
