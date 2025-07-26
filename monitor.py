# Package: cognize
# File: monitor.py

from .core import RCC
from .mutation import mutate_reception
from .history import SaveManager
from .utils import scalar_drift, semantic_drift, get_embedding

class RCCMonitor:
    def __init__(self, mode="scalar", rupture_mutation=True, drift_threshold=None, embed_fn=None):
        """
        RCCMonitor initializes a rupture-aware cognitive loop.

        Parameters:
        - mode: 'scalar' or 'semantic'
        - rupture_mutation: whether to mutate R(t) post-rupture
        - drift_threshold: optional override for Θ(t)
        - embed_fn: function to convert text to vector (for semantic drift)
        """
        self.rcc = RCC()
        self.history = SaveManager()
        self.mode = mode
        self.rupture_mutation = rupture_mutation
        self.embed_fn = embed_fn or get_embedding
        self.drift_fn = scalar_drift if mode == "scalar" else semantic_drift
        self.override_threshold = drift_threshold

    def observe(self, prompt, response):
        """
        Accepts a prompt and response pair. Computes drift, updates RCC, logs trace.
        Returns a dict with updated RCC state and rupture flag.
        """
        V_prev = self.rcc.V
        R_t = response

        # Compute ∆(t)
        delta = self.drift_fn(V_prev, R_t, self.embed_fn)

        # Override threshold if specified
        theta = self.override_threshold or self.rcc.rupture_threshold()

        if delta > theta:
            self.rcc.V = self.rcc.V0
            self.rcc.E = 0
            rupture = True

            if self.rupture_mutation:
                S_bar = self.rcc.project_divergence(R_t, V_prev)
                R_t = mutate_reception(R_t, S_bar, self.rcc.E)
        else:
            k = 0.5  # simple realignment scaling
            self.rcc.V = V_prev + k * delta * (1 + self.rcc.E)
            self.rcc.E += self.rcc.c * delta
            rupture = False

        S_bar = self.rcc.project_divergence(R_t, V_prev)
        self.history.add_point(self.rcc.V, R_t, delta, theta, self.rcc.E, S_bar, rupture)

        return {
            "V": self.rcc.V,
            "R": R_t,
            "∆": delta,
            "Θ": theta,
            "E": self.rcc.E,
            "S̄": S_bar,
            "rupture": rupture
        }

    def trace(self):
        return self.history.all_points()

    def last_state(self):
        return self.history.get_point(len(self.history.timeline) - 1)
