# src/visualizers/wireframe_drawer.py
import mediapipe as mp
import numpy as np

class WireframeDrawer:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic

    def draw(self, frame, results):
        black_image = np.zeros_like(frame)

        # Pose
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                black_image,
                results.pose_landmarks,
                self.mp_holistic.POSE_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=2)
            )

        # Face
        if results.face_landmarks:
            self.mp_drawing.draw_landmarks(
                black_image,
                results.face_landmarks,
                self.mp_holistic.FACEMESH_TESSELATION,
                self.mp_drawing.DrawingSpec(color=(255,255,0), thickness=1, circle_radius=1),
                self.mp_drawing.DrawingSpec(color=(255,0,0), thickness=1)
            )

        # Left Hand
        if results.left_hand_landmarks:
            self.mp_drawing.draw_landmarks(
                black_image,
                results.left_hand_landmarks,
                self.mp_holistic.HAND_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(0,255,255), thickness=2, circle_radius=2),
                self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=2)
            )

        # Right Hand
        if results.right_hand_landmarks:
            self.mp_drawing.draw_landmarks(
                black_image,
                results.right_hand_landmarks,
                self.mp_holistic.HAND_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(0,255,255), thickness=2, circle_radius=2),
                self.mp_drawing.DrawingSpec(color=(0,0,255), thickness=2)
            )

        return black_image
