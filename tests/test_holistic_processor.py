import unittest
import cv2
from processors.holistic_processor import HolisticProcessor

class TestHolisticProcessor(unittest.TestCase):
    def test_landmarks_detection(self):
        processor = HolisticProcessor()
        frame = cv2.imread('tests/sample_image.jpg')  # Use a small test image
        results = processor.process(frame)
        self.assertIsNotNone(results)
        processor.close()
