import unittest
import numpy as np
from visualizers.wireframe_drawer import WireframeDrawer

class TestWireframeDrawer(unittest.TestCase):
    def test_draw(self):
        drawer = WireframeDrawer()
        dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        result_frame = drawer.draw(dummy_frame, None)
        self.assertEqual(result_frame.shape, dummy_frame.shape)
