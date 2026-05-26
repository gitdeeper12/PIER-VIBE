"""k-ω SST turbulence closure model."""

import numpy as np


class TurbulenceModel:
    """k-ω SST turbulence model."""
    
    def __init__(self):
        self.beta_star = 0.09
        self.alpha = 5.0 / 9.0
        self.beta = 0.075
        self.sigma_k = 0.5
        self.sigma_omega = 0.5
        
    def turbulent_viscosity(self, k: np.ndarray, omega: np.ndarray) -> np.ndarray:
        """μ_t = ρ·k/ω"""
        return k / omega
    
    def production(self, S: np.ndarray, k: np.ndarray) -> np.ndarray:
        """P_k = μ_t·S²"""
        mu_t = self.turbulent_viscosity(k, k / 0.01)
        return mu_t * S**2
    
    def transport_k(self, k: np.ndarray, omega: np.ndarray, 
                    P_k: np.ndarray, dt: float) -> np.ndarray:
        """∂(ρk)/∂t = P_k - β*ρωk + ∇·[(μ + σ_k μ_t)∇k]"""
        dissipation = self.beta_star * k * omega
        diffusion = np.gradient(np.gradient(k))
        return k + dt * (P_k - dissipation + diffusion)
    
    def transport_omega(self, omega: np.ndarray, k: np.ndarray,
                        P_k: np.ndarray, dt: float) -> np.ndarray:
        """∂(ρω)/∂t = αρS² - βρω² + ∇·[(μ + σ_ω μ_t)∇ω] + cross_diff"""
        production = self.alpha * P_k
        dissipation = self.beta * omega**2
        diffusion = np.gradient(np.gradient(omega))
        return omega + dt * (production - dissipation + diffusion)
