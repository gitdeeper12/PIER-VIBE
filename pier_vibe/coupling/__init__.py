"""Fluid-Structure-Soil coupling module.

Components:
- Arbitrary Lagrangian-Eulerian (ALE) formulation
- Added mass computation
- Added damping computation
- Biot consolidation for soil coupling
"""

from .ale import ALEFormulation
from .added_mass import AddedMass
from .added_damping import AddedDamping
from .biot import BiotConsolidation

__all__ = ["ALEFormulation", "AddedMass", "AddedDamping", "BiotConsolidation"]
