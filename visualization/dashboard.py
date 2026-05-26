"""Main bridge safety dashboard layout."""

import streamlit as st
import plotly.graph_objects as go
import numpy as np


class Dashboard:
    """Main dashboard for PIER-VIBE real-time monitoring."""
    
    def __init__(self):
        self.bshi = 0.92
        self.scour_depth = 1.8
        self.fatigue_damage = 0.35
        self.freq_drift = 2.1
        
    def render(self):
        """Render the full dashboard."""
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("BSHI", f"{self.bshi:.3f}", delta="≥0.85")
        with col2:
            st.metric("Scour Depth", f"{self.scour_depth:.1f} m", delta="≤4.2 m")
        with col3:
            st.metric("Fatigue Damage", f"{self.fatigue_damage:.2f}", delta="≤0.80")
        with col4:
            st.metric("Frequency Drift", f"{self.freq_drift:.1f}%", delta="≤5.0%")
        
        tab1, tab2, tab3 = st.tabs(["Scour Evolution", "Frequency Drift", "Fatigue Forecast"])
        
        with tab1:
            self._render_scour_map()
        with tab2:
            self._render_frequency_plot()
        with tab3:
            self._render_fatigue_plot()
    
    def _render_scour_map(self):
        """Render scour hole evolution heatmap."""
        fig = go.Figure()
        x = np.linspace(-10, 10, 50)
        y = np.linspace(-10, 10, 50)
        X, Y = np.meshgrid(x, y)
        Z = 4.2 * np.exp(-((X)**2 + (Y)**2) / (2 * 3**2))
        
        fig.add_trace(go.Heatmap(z=Z, x=x, y=y, colorscale='RdBu'))
        fig.update_layout(title="Scour Hole Evolution", height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_frequency_plot(self):
        """Render frequency drift plot."""
        fig = go.Figure()
        time = np.arange(0, 24, 0.5)
        freq = 0.85 + 0.02 * np.sin(time / 24 * np.pi) + 0.01 * time / 24
        
        fig.add_trace(go.Scatter(x=time, y=freq, mode='lines', name='Natural Frequency'))
        fig.add_hline(y=0.85, line_dash="dash", line_color="red")
        fig.update_layout(title="Natural Frequency Drift", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_fatigue_plot(self):
        """Render fatigue accumulation plot."""
        fig = go.Figure()
        cycles = np.arange(0, 1e6, 50000)
        damage = 1 - np.exp(-cycles / 2e6)
        
        fig.add_trace(go.Scatter(x=cycles, y=damage, mode='lines', name='Cumulative Damage'))
        fig.add_hline(y=0.80, line_dash="dash", line_color="red")
        fig.update_layout(title="Fatigue Damage Accumulation", height=400)
        st.plotly_chart(fig, use_container_width=True)
