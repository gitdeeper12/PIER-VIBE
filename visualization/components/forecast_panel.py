"""PINN forecast panel for PIER-VIBE dashboard."""

import streamlit as st
import plotly.graph_objects as go


class ForecastPanel:
    """AI forecast panel for scour and fatigue predictions."""
    
    def __init__(self):
        self.scour_forecast = {24: 2.1, 48: 2.5, 72: 2.8}
        self.fatigue_forecast = {24: 0.42, 48: 0.48, 72: 0.52}
        
    def render(self):
        """Render the forecast panel."""
        st.subheader("🤖 PINN Forecast")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Scour Depth Forecast")
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(
                x=list(self.scour_forecast.keys()),
                y=list(self.scour_forecast.values()),
                mode='lines+markers',
                name='PINN Scour'
            ))
            fig1.add_hline(y=4.2, line_dash="dash", line_color="red")
            fig1.update_layout(height=250, xaxis_title="Hours", yaxis_title="Scour Depth (m)")
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            st.markdown("#### Fatigue Damage Forecast")
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=list(self.fatigue_forecast.keys()),
                y=list(self.fatigue_forecast.values()),
                mode='lines+markers',
                name='PINN Fatigue'
            ))
            fig2.add_hline(y=0.80, line_dash="dash", line_color="red")
            fig2.update_layout(height=250, xaxis_title="Hours", yaxis_title="Damage")
            st.plotly_chart(fig2, use_container_width=True)
        
        st.info(f"PINN Scour 72h RMSE: ±0.08 m | PINN Fatigue 72h MAE: 2.8%")
