# src/camera/webcam.py
import cv2

class Webcam:
    def __init__(self, camera_id=0, flip=True):
        self.camera_id = camera_id
        self.flip = flip
        self.cap = cv2.VideoCapture(self.camera_id)
        if not self.cap.isOpened():
            raise ValueError(f"Error: Cannot open webcam {self.camera_id}")

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Error: Failed to capture frame from webcam")
        if self.flip:
            frame = cv2.flip(frame, 1)
        return frame

    def release(self):
        self.cap.release()
