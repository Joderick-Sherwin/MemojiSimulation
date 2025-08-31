import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import cv2
from camera.webcam import Webcam
from processors.holistic_processor import HolisticProcessor
from visualizers.wireframe_drawer import WireframeDrawer
import numpy as np

class TestIntegration(unittest.TestCase):
    def test_pipeline(self):
        cam = Webcam(0)
        processor = HolisticProcessor()
        drawer = WireframeDrawer()
        frame = cam.read_frame()
        results = processor.process(frame)
        combined_frame = cv2.hconcat([frame, drawer.draw(frame, results)])
        self.assertEqual(combined_frame.shape[0], frame.shape[0])
        cam.release()
        processor.close()

if __name__ == "__main__":
    unittest.main()
