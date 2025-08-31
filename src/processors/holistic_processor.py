# src/processors/holistic_processor.py
import mediapipe as mp

class HolisticProcessor:
    def __init__(self, model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            static_image_mode=False,
            model_complexity=model_complexity,
            smooth_landmarks=True,
            enable_segmentation=False,
            refine_face_landmarks=True,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def process(self, frame):
        # Convert BGR to RGB and process
        return self.holistic.process(frame[:, :, ::-1])  # BGR->RGB

    def close(self):
        self.holistic.close()
