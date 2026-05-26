"""Biot consolidation for soil-structure coupling."""

import numpy as np


class BiotConsolidation:
    """Biot's theory of consolidation for saturated porous media."""
    
    def __init__(self, K_dr: float = 100e6, K_s: float = 200e6):
        self.K_dr = K_dr  # Drained bulk modulus (Pa)
        self.K_s = K_s    # Solid grain bulk modulus (Pa)
        
    def biot_coefficient(self) -> float:
        """α_B = 1 - K_dr/K_s"""
        return 1.0 - self.K_dr / self.K_s
    
    def consolidation_equation(self, u: np.ndarray, p: np.ndarray, 
                                dt: float, k: float = 1e-7) -> np.ndarray:
        """m_v·∂u/∂t = k/γ_w·∇²u - ∂ε_v/∂t"""
        m_v = 1e-5  # Coefficient of volume compressibility
        gamma_w = 9.81
        
        laplacian = np.gradient(np.gradient(p))
        du_dt = (k / gamma_w * laplacian - self._strain_rate()) / m_v
        
        return u + dt * du_dt
    
    def _strain_rate(self) -> float:
        """Volumetric strain rate ∂ε_v/∂t"""
        return 1e-6
    
    def effective_stress(self, sigma: float, p: float) -> float:
        """σ' = σ - α_B·p"""
        alpha = self.biot_coefficient()
        return sigma - alpha * p
    
    undrained_bulk_modulus(self) -> float:
        """Undrained bulk modulus K_u = K_dr + α_B²·K_s·K_dr/(K_s - K_dr)"""
        alpha = self.biot_coefficient()
        return self.K_dr + alpha**2 * self.K_s * self.K_dr / (self.K_s - self.K_dr)
