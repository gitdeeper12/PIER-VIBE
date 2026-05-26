"""SSSE scour mechanics subsystem.

Components:
- Melville-Coleman scour rate equation
- Bed shear stress computation
- Horseshoe vortex amplification
- Equilibrium scour depth (HEC-18)
"""

from .melville_coleman import MelvilleColeman
from .bed_shear import BedShear
from .horseshoe import HorseshoeAmplification
from .equilibrium_depth import EquilibriumDepth

__all__ = ["MelvilleColeman", "BedShear", "HorseshoeAmplification", "EquilibriumDepth"]
