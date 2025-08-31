# MemojiSimulation

MemojiSimulation is a Python application that captures webcam video, processes full-body pose, face, and hand landmarks using MediaPipe's Holistic model, and visualizes the results as a wireframe overlay. The project is modular, configurable, and supports video recording and analytics.

---

## Features

- **Webcam Capture:** Real-time video stream from your webcam.
- **Holistic Pose Processing:** Uses MediaPipe Holistic for body, face, and hand landmark detection.
- **Wireframe Visualization:** Draws detected landmarks and connections as a wireframe overlay.
- **Video Recording:** Optionally records the processed video to disk.
- **Analytics:** Framework for pose data analysis (extensible).
- **Configurable:** YAML-based configuration for camera, model, visualization, and logging.
- **Logging:** Detailed logging of application events and frame processing.

---

## Folder Structure

```
MemojiSimulation/
├── assets/                  # (Assets for visualization, if any)
├── config/
│   ├── config.yaml          # Main application configuration
│   └── logging_config.yaml  # Logging configuration
├── logs/
│   └── app.log              # Application log file
├── notebooks/               # (Jupyter notebooks, if any)
├── recordings/
│   └── output.avi           # Example output video
├── src/
│   ├── main.py              # Application entry point
│   ├── camera/
│   │   └── webcam.py        # Webcam capture class
│   ├── processors/
│   │   └── holistic_processor.py # MediaPipe holistic processor
│   ├── services/
│   │   ├── analytics.py     # Analytics service (pose data analysis)
│   │   └── recorder.py      # Video recorder
│   ├── utils/
│   │   ├── helpers.py       # Utility functions
│   │   └── logger.py        # Logger setup
│   └── visualizers/
│       └── wireframe_drawer.py # Wireframe drawing logic
├── tests/
│   ├── test_camera.py
│   ├── test_holistic_processor.py
│   └── test_wireframe_drawer.py
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Webcam

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/MemojiSimulation.git
   cd MemojiSimulation
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Configuration

- **Edit `config/config.yaml`** to adjust camera settings, holistic model options, visualization parameters, and recorder options.
- **Edit `config/logging_config.yaml`** to customize logging behavior.

### Running the Application

```sh
python src/main.py
```

- The application will open your webcam, process frames, and display the wireframe overlay.
- Press the configured exit key (default: `q`) to close the application.

---

## Modules Overview

- **src/main.py:** Orchestrates the application: loads config, sets up logging, initializes modules, and runs the main loop.
- **camera/webcam.py:** Handles webcam initialization and frame capture.
- **processors/holistic_processor.py:** Wraps MediaPipe Holistic for landmark detection.
- **visualizers/wireframe_drawer.py:** Draws pose, face, and hand wireframes on frames.
- **services/recorder.py:** Records processed video to disk.
- **services/analytics.py:** (Stub) For pose data analytics.
- **utils/helpers.py:** Utility functions (e.g., frame resizing, YAML loading).
- **utils/logger.py:** Logger setup using YAML config.

---

## Logging

- Logs are written to `logs/app.log`.
- Logging configuration is controlled via `config/logging_config.yaml`.

---

## Testing

- Unit test stubs are provided in the `tests/` directory.
- To run tests (after implementing them):
  ```sh
  pytest tests/
  ```

---

## Dependencies

- [MediaPipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [PyYAML](https://pyyaml.org/) (for config parsing)

Install all dependencies using:
```sh
pip install -r requirements.txt
```

---

## Customization

- **Wireframe Appearance:** Tweak colors, thickness, and visibility in `config/config.yaml`.
- **Analytics:** Extend `services/analytics.py` for custom pose/gesture analysis.
- **Recording:** Enable/disable or change output path in the config.

---

## Acknowledgements

- Built with [MediaPipe](https://google.github.io/mediapipe/) and [OpenCV](https://opencv.org/).

---

## Contact

For questions or contributions, open an issue or contact [your-email@example.com].
