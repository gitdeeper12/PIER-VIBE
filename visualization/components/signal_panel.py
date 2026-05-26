"""Safety signal panel component for PIER-VIBE dashboard."""

import streamlit as st


class SignalPanel:
    """Safety signal panel with 🟢🟠🔴 indicators."""
    
    SIGNALS = {
        "STABILITY_CERTIFIED": {"icon": "🟢", "color": "green", "message": "Normal operation — all constraints satisfied"},
        "MONITORING_PHASE": {"icon": "🟠", "color": "orange", "message": "Reduced operations — PINN forecast active"},
        "STOP_COMMAND": {"icon": "🔴", "color": "red", "message": "Bridge closure — emergency inspection required"}
    }
    
    def __init__(self):
        self.current_signal = "STABILITY_CERTIFIED"
        self.bshi = 0.92
        
    def render(self):
        """Render the signal panel."""
        signal = self.SIGNALS.get(self.current_signal)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.markdown(f"<h1 style='text-align: center;'>{signal['icon']}</h1>", 
                       unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<h3 style='text-align: center;'>{self.current_signal}</h3>",
                       unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'>{signal['message']}</p>",
                       unsafe_allow_html=True)
        
        with col3:
            st.metric("BSHI", f"{self.bshi:.3f}", delta="≥0.85")
        
        st.progress(min(self.bshi, 1.0))
        
    def update(self, signal: str, bshi: float):
        """Update signal panel values."""
        self.current_signal = signal
        self.bshi = bshi
