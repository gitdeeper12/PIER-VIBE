"""PIER-VIBE: Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments

A Critical Framework for Subsurface Scour Mechanics, Dynamic Wave-Structure Interaction,
and Resonance Fatigue Governance in Offshore and Riverine Bridges
"""

__version__ = "1.0.0"
__author__ = "Samir Baladi"
__email__ = "gitdeeper@gmail.com"
__doi__ = "10.5281/zenodo.20390646"

from .pipeline import BridgeGovernor
from .safety import SafetyCertifier

__all__ = ["BridgeGovernor", "SafetyCertifier"]
