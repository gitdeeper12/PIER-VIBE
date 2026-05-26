"""Adaptive finite element mesh generation."""

import numpy as np


class MeshGenerator:
    """Finite element mesh with adaptive refinement."""
    
    def __init__(self, n_elements: int = 100000):
        self.n_elements = n_elements
        self.nodes = None
        self.elements = None
        
    def generate_cylinder_mesh(self, radius: float, height: float, length: float) -> tuple:
        """Generate cylinder mesh for bridge pier."""
        n_r = int(np.sqrt(self.n_elements / 2))
        n_z = n_r
        
        r = np.linspace(0, radius, n_r)
        z = np.linspace(-height/2, height/2, n_z)
        
        R, Z = np.meshgrid(r, z)
        X = R * np.cos(np.linspace(0, 2*np.pi, n_r)[:, None])
        Y = R * np.sin(np.linspace(0, 2*np.pi, n_r)[:, None])
        
        self.nodes = np.column_stack((X.flatten(), Y.flatten(), Z.flatten()))
        return self.nodes, self.elements
    
    def generate_fluid_mesh(self, domain_size: tuple) -> np.ndarray:
        """Generate fluid domain mesh."""
        nx, ny, nz = 50, 30, 20
        x = np.linspace(0, domain_size[0], nx)
        y = np.linspace(0, domain_size[1], ny)
        z = np.linspace(0, domain_size[2], nz)
        
        X, Y, Z = np.meshgrid(x, y, z)
        self.nodes = np.column_stack((X.flatten(), Y.flatten(), Z.flatten()))
        return self.nodes
    
    def get_element_centroids(self) -> np.ndarray:
        """Get centroids of all elements."""
        if self.nodes is None:
            return np.array([])
        return np.mean(self.nodes, axis=0).reshape(1, -1)
