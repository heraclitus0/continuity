# Package: cognize
# File: mutation.py

import numpy as np

def mutate_reception(R_t, S_bar, E, gamma=0.1, noise_scale=0.02):
    """
    Mutates the reception R(t) post-rupture by injecting directional drift.

    Parameters:
    - R_t: original reception
    - S_bar: projected divergence direction (+1, -1, or 0)
    - E: accumulated misalignment
    - gamma: scaling factor for hallucination magnitude
    - noise_scale: Gaussian noise factor

    Returns:
    - Mutated R'(t+1)
    """
    hallucination_drift = gamma * E * S_bar
    noise = np.random.normal(0, noise_scale)
    return R_t + hallucination_drift + noise
