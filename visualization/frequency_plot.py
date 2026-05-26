"""Natural frequency drift visualization."""

import plotly.graph_objects as go
import numpy as np


class FrequencyPlot:
    """Frequency drift over time visualization."""
    
    @staticmethod
    def render(frequencies: list, time_hours: list, f0: float = 0.85) -> go.Figure:
        """Render frequency drift plot."""
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_hours, y=frequencies, mode='lines', name='Natural Frequency'))
        fig.add_hline(y=f0, line_dash="dash", line_color="red", annotation_text=f"Initial f₀ = {f0} Hz")
        fig.add_hline(y=f0 * 0.95, line_dash="dot", line_color="orange", annotation_text="Warning")
        fig.update_layout(title="Natural Frequency Drift Monitoring", height=400)
        return fig
