# src/utils/helpers.py
import cv2
import yaml

def resize_frame(frame, width=None, height=None):
    """Resize frame keeping aspect ratio."""
    if width is None and height is None:
        return frame
    h, w = frame.shape[:2]
    if width is None:
        ratio = height / float(h)
        width = int(w * ratio)
    elif height is None:
        ratio = width / float(w)
        height = int(h * ratio)
    return cv2.resize(frame, (width, height))

def load_config(config_file):
    """Load YAML configuration."""
    import os
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
    return config
