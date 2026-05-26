"""Streamlit application entry point for PIER-VIBE."""

import streamlit as st
from .dashboard import Dashboard


def main():
    st.set_page_config(
        page_title="PIER-VIBE Bridge Safety Dashboard",
        page_icon="🌉",
        layout="wide"
    )
    
    st.title("🌉 PIER-VIBE Bridge Safety Dashboard")
    st.caption("Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments")
    
    dashboard = Dashboard()
    dashboard.render()


if __name__ == "__main__":
    main()
