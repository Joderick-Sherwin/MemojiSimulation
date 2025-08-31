# src/services/analytics.py
import numpy as np

class Analytics:
    def __init__(self):
        self.data = []

    def record_pose(self, landmarks):
        """Store pose landmarks for later analysis"""
        if landmarks:
            self.data.append([(lm.x, lm.y, lm.z) for lm in landmarks.landmark])

    def compute_statistics(self):
        """Compute simple statistics (example: average landmark positions)"""
        if not self.data:
            return None
        return np.mean(np.array(self.data), axis=0)
