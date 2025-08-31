import cv2
import os

class Recorder:
    def __init__(self, output_dir="recordings", filename="output.mp4", fps=30):
        self.output_dir = output_dir
        self.filename = filename
        self.fps = fps
        self.writer = None
        self.frame_size = None

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.filepath = os.path.join(self.output_dir, self.filename)

    def start(self, first_frame):
        """Initialize VideoWriter using the first frame's dimensions."""
        if first_frame is None:
            raise ValueError("First frame must be provided to determine video size.")

        self.frame_size = (first_frame.shape[1], first_frame.shape[0])  # (width, height)

        # Codec selection
        if self.filename.lower().endswith(".mp4"):
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
        else:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')  # fallback for AVI

        self.writer = cv2.VideoWriter(self.filepath, fourcc, self.fps, self.frame_size)

        if not self.writer.isOpened():
            raise RuntimeError(f"Failed to open video writer: {self.filepath}")

    def write(self, frame):
        """Write a frame to the video file without resizing."""
        if self.writer is None:
            raise RuntimeError("Recorder not started. Call start() with the first frame first.")
        self.writer.write(frame)

    def stop(self):
        """Release the video writer."""
        if self.writer:
            self.writer.release()
            self.writer = None
