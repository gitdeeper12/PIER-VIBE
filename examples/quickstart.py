#!/usr/bin/env python3
"""Quick start example for PIER-VIBE."""

from pier_vibe import BridgeGovernor


def main():
    print("=" * 50)
    print("PIER-VIBE Quick Start Example")
    print("=" * 50)
    
    governor = BridgeGovernor(
        bridge_config="configs/offshore_monopile.yaml",
        water_depth_m=25.0,
        sensor_stream="live"
    )
    
    result = governor.evaluate()
    
    print(f"\n📊 Results:")
    print(f"  Safety Signal: {result.signal.value}")
    print(f"  BSHI: {result.bshi:.3f}")
    print(f"  Scour Depth: {result.scour_depth_m:.1f} m")
    print(f"  Fatigue Damage: {result.fatigue_damage:.2f}")
    print(f"  Frequency Drift: {result.frequency_drift_pct:.1f}%")
    print(f"  Governance Level: {result.governance_level}")


if __name__ == "__main__":
    main()
