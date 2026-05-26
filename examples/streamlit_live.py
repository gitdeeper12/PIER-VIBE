#!/usr/bin/env python3
"""Launch Streamlit live dashboard for PIER-VIBE."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    import streamlit as st
    from visualization.dashboard import Dashboard
    
    st.set_page_config(
        page_title="PIER-VIBE Live Dashboard",
        page_icon="🌉",
        layout="wide"
    )
    
    st.title("🌉 PIER-VIBE Live Dashboard")
    dashboard = Dashboard()
    dashboard.render()


if __name__ == "__main__":
    main()
