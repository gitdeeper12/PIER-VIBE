#!/usr/bin/env python3
"""AI forecast demonstration for PIER-VIBE."""

from pier_vibe.ai import PINNScourForecaster, PINNFatigueForecaster, BSHICalculator


def main():
    print("=" * 50)
    print("PIER-VIBE AI Forecast Demo")
    print("=" * 50)
    
    pinn_scour = PINNScourForecaster.from_pretrained()
    print(f"PINN Scour 72h prediction: {pinn_scour.predict(None):.2f} m")
    print(f"PINN Scour RMSE: ±{pinn_scour.RMSE_72H:.2f} m")
    
    pinn_fatigue = PINNFatigueForecaster.from_pretrained()
    print(f"PINN Fatigue 72h prediction: {pinn_fatigue.predict(None):.2f}")
    print(f"PINN Fatigue MAE: {pinn_fatigue.MAE_72H:.1%}")
    
    bshi = BSHICalculator.from_pretrained()
    bshi_value = bshi.compute(1.8, 0.35, 2.1)
    print(f"BSHI: {bshi_value:.3f}")
    print(f"BSHI Precision: {bshi.PRECISION}")


if __name__ == "__main__":
    main()
