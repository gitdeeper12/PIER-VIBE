"""Six canonical bridge configurations for validation."""

from dataclasses import dataclass


@dataclass
class BridgeScenario:
    name: str
    water_depth_m: float
    pier_diameter_m: float
    d50_mm: float
    sediment_type: str
    expected_bshi: float


class BridgeScenarios:
    """Six benchmark scenarios from paper validation."""
    
    B1 = BridgeScenario(
        name="B1_SinglePier_Sand",
        water_depth_m=8.0,
        pier_diameter_m=2.5,
        d50_mm=0.5,
        sediment_type="sand",
        expected_bshi=0.972
    )
    
    B2 = BridgeScenario(
        name="B2_TwinPier_Gravel",
        water_depth_m=12.0,
        pier_diameter_m=3.0,
        d50_mm=2.0,
        sediment_type="gravel",
        expected_bshi=0.965
    )
    
    B3 = BridgeScenario(
        name="B3_OffshoreMonopile_Sand",
        water_depth_m=25.0,
        pier_diameter_m=3.5,
        d50_mm=0.5,
        sediment_type="sand",
        expected_bshi=0.978
    )
    
    B4 = BridgeScenario(
        name="B4_JacketFoundation_RockClay",
        water_depth_m=30.0,
        pier_diameter_m=4.0,
        d50_mm=10.0,
        sediment_type="rock-clay",
        expected_bshi=0.959
    )
    
    B5 = BridgeScenario(
        name="B5_CableStayed_Composite",
        water_depth_m=18.0,
        pier_diameter_m=3.0,
        d50_mm=0.5,
        sediment_type="sand",
        expected_bshi=0.968
    )
    
    B6 = BridgeScenario(
        name="B6_Suspension_DeepWater",
        water_depth_m=40.0,
        pier_diameter_m=5.0,
        d50_mm=0.5,
        sediment_type="sand",
        expected_bshi=0.971
    )
    
    @classmethod
    def get_all(cls):
        return [cls.B1, cls.B2, cls.B3, cls.B4, cls.B5, cls.B6]
