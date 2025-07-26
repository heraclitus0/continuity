# Package: cognize
# File: core.py

import numpy as np

class RCC:
    def __init__(self, V0=0.0, E0=0.0, a=0.1, c=0.05, sigma=0.01):
        """
        RCC engine stores the current projection (V), misalignment memory (E),
        and rupture parameters (a: rupture slope, c: memory accumulation, sigma: noise).
        """
        self.V0 = V0  # Reset baseline
        self.V = V0   # Current projection
        self.E = E0   # Misalignment memory
        self.a = a    # Threshold scaling factor
        self.c = c    # Memory accumulation constant
        self.sigma = sigma  # Noise factor

    def rupture_threshold(self):
        """Compute Θ(t) based on E(t) and noise."""
        noise = np.random.normal(0, self.sigma)
        return self.a * self.E + noise + 0.2  # Base offset 0.2 to avoid trivial rupture

    def project_divergence(self, R, V):
        """
        Compute projected divergence S̄(t):
        +1 if R > V (overextension), -1 if R < V (collapse), 0 if aligned
        """
        return np.sign(R - V)

    def reset(self):
        """Hard reset the RCC state."""
        self.V = self.V0
        self.E = 0
