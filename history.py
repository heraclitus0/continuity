# Package: cognize
# File: history.py

class SavePoint:
    def __init__(self, idx, V, R, delta, theta, E, S_bar, rupture):
        self.idx = idx
        self.V = V
        self.R = R
        self.delta = delta
        self.theta = theta
        self.E = E
        self.S_bar = S_bar
        self.rupture = rupture

    def as_dict(self):
        return {
            "idx": self.idx,
            "V": self.V,
            "R": self.R,
            "∆": self.delta,
            "Θ": self.theta,
            "E": self.E,
            "S̄": self.S_bar,
            "rupture": self.rupture
        }


class SaveManager:
    def __init__(self):
        self.timeline = []

    def add_point(self, V, R, delta, theta, E, S_bar, rupture):
        idx = len(self.timeline)
        point = SavePoint(idx, V, R, delta, theta, E, S_bar, rupture)
        self.timeline.append(point)

    def get_point(self, idx):
        if 0 <= idx < len(self.timeline):
            return self.timeline[idx]
        return None

    def all_points(self):
        return [p.as_dict() for p in self.timeline]

    def reset(self):
        self.timeline = []
