import unittest
from camera.webcam import Webcam

class TestWebcam(unittest.TestCase):
    def test_capture_frame(self):
        cam = Webcam(0)
        frame = cam.read_frame()
        self.assertIsNotNone(frame)
        self.assertEqual(len(frame.shape), 3)  # Should be a color image
        cam.release()
