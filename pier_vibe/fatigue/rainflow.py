"""Rainflow cycle counting algorithm for stress histories."""

import numpy as np


class RainflowCounter:
    """Rainflow cycle counting for variable amplitude loading."""
    
    def __init__(self):
        pass
    
    def count(self, stress_history: np.ndarray) -> tuple:
        """Extract cycles and amplitudes from stress history."""
        # Simplified rainflow algorithm
        peaks = self._extract_peaks(stress_history)
        cycles = []
        amplitudes = []
        
        for i in range(1, len(peaks) - 1):
            amplitude = abs(peaks[i] - peaks[i-1]) / 2
            amplitudes.append(amplitude)
            cycles.append(1)
            
        return cycles, amplitudes
    
    def _extract_peaks(self, data: np.ndarray) -> np.ndarray:
        """Extract peak and valley points."""
        peaks = []
        for i in range(1, len(data) - 1):
            if (data[i] > data[i-1] and data[i] > data[i+1]) or \
               (data[i] < data[i-1] and data[i] < data[i+1]):
                peaks.append(data[i])
        
        if len(peaks) == 0:
            peaks = [data[0], data[-1]]
        
        return np.array(peaks)
    
    def half_cycle_counting(self, data: np.ndarray) -> list:
        """Simplified half-cycle counting."""
        half_cycles = []
        for i in range(1, len(data)):
            half_cycles.append(abs(data[i] - data[i-1]))
        return half_cycles
    
    def range_mean_pair(self, cycles: list, amplitudes: list) -> list:
        """Pair cycles with their mean stresses."""
        return list(zip(cycles, amplitudes))
