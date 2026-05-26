"""Unit tests for PIER-VIBE main pipeline."""

import unittest
from pier_vibe import BridgeGovernor
from pier_vibe.safety import SafetySignal


class TestPipeline(unittest.TestCase):
    """Test cases for PIER-VIBE main pipeline."""
    
    def setUp(self):
        self.governor = BridgeGovernor(
            bridge_config="configs/offshore_monopile.yaml",
            water_depth_m=25.0,
            sensor_stream="live"
        )
    
    def test_initialization(self):
        self.assertEqual(self.governor.water_depth_m, 25.0)
        self.assertEqual(self.governor.BSHI_MIN, 0.85)
    
    def test_evaluate(self):
        result = self.governor.evaluate()
        self.assertIsNotNone(result.signal)
        self.assertGreater(result.bshi, 0)
        self.assertGreater(result.scour_depth_m, 0)
        self.assertGreater(result.fatigue_damage, 0)
    
    def test_bshi_computation(self):
        bshi = self.governor._compute_bshi(1.8, 0.35, 2.1)
        self.assertGreater(bshi, 0)
        self.assertLessEqual(bshi, 1.0)
    
    def test_transient_run(self):
        from pier_vibe.simulation import BridgeScenarios
        scenario = BridgeScenarios.B1
        results = self.governor.run_transient(scenario)
        self.assertIsNotNone(results.max_scour_depth)


if __name__ == '__main__':
    unittest.main()
