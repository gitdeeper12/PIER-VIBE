"""Fatigue damage accumulation visualization."""

import plotly.graph_objects as go
import numpy as np


class FatigueDamagePlot:
    """Cumulative fatigue damage display."""
    
    @staticmethod
    def render(damage_history: list, cycles: list) -> go.Figure:
        """Render fatigue damage accumulation plot."""
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=cycles, y=damage_history, mode='lines', name='Cumulative Damage'))
        fig.add_hline(y=0.80, line_dash="dash", line_color="red", annotation_text="Warning Threshold")
        fig.add_hline(y=1.0, line_dash="dash", line_color="darkred", annotation_text="Failure")
        fig.update_layout(title="Palmgren-Miner Fatigue Damage Accumulation", height=400)
        return fig
