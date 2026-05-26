"""Scour hole evolution heatmap visualization."""

import plotly.graph_objects as go
import numpy as np


class ScourMap:
    """Scour hole depth visualization."""
    
    @staticmethod
    def render(scour_depth: float, D_pier: float = 3.5) -> go.Figure:
        """Render scour hole heatmap."""
        x = np.linspace(-10, 10, 50)
        y = np.linspace(-10, 10, 50)
        X, Y = np.meshgrid(x, y)
        
        # Gaussian scour hole profile
        Z = scour_depth * np.exp(-((X)**2 + (Y)**2) / (2 * (D_pier)**2))
        
        fig = go.Figure()
        fig.add_trace(go.Heatmap(z=Z, x=x, y=y, colorscale='RdBu'))
        fig.update_layout(title=f"Scour Hole (max depth = {scour_depth:.2f} m)", height=500)
        return fig
