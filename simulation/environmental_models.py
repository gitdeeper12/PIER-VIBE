"""Environmental loading models for bridge scenarios."""

import numpy as np


class EnvironmentalModels:
    """Wave, current, and wind profiles."""
    
    @staticmethod
    def jonswap_spectrum(Hs: float, Tp: float, f: np.ndarray) -> np.ndarray:
        """JONSWAP wave spectrum."""
        alpha = 0.076
        fp = 1 / Tp
        sigma = 0.07 if f <= fp else 0.09
        gamma = 3.3
        
        S = alpha * 9.81**2 * (2*np.pi)**(-4) * f**(-5) * np.exp(-1.25 * (f/fp)**(-4))
        S *= gamma**np.exp(-(f/fp - 1)**2 / (2 * sigma**2))
        return S
    
    @staticmethod
    def current_profile(z: np.ndarray, u_surface: float, depth: float) -> np.ndarray:
        """Power law current profile."""
        return u_surface * (z / depth)**0.15
    
    @staticmethod
    def wind_profile(z: np.ndarray, u_ref: float, z_ref: float = 10.0) -> np.ndarray:
        """Logarithmic wind profile."""
        z0 = 0.01
        kappa = 0.41
        return u_ref * np.log(z / z0) / np.log(z_ref / z0)
    
    @staticmethod
    def flood_hydrograph(peak_time_hours: float = 24, duration_hours: float = 72) -> np.ndarray:
        """Flood event hydrograph."""
        t = np.linspace(0, duration_hours, 1000)
        u = np.exp(-(t - peak_time_hours)**2 / (2 * (duration_hours/6)**2))
        return t, u
    
    @staticmethod
    def wave_timeseries(Hs: float, Tp: float, duration_sec: float, dt: float = 0.1) -> np.ndarray:
        """Wave elevation time series."""
        t = np.arange(0, duration_sec, dt)
        eta = Hs/2 * np.sin(2*np.pi/Tp * t)
        return t, eta
