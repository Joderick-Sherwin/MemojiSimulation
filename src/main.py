import logging
import time

# -------------------------
# Log imports
# -------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FullBodyWireframe_Imports")

logger.info("Importing cv2")
import cv2
logger.info("cv2 imported successfully")

logger.info("Importing load_config from utils.helpers")
from utils.helpers import load_config
logger.info("load_config imported successfully")

logger.info("Importing setup_logger from utils.logger")
from utils.logger import setup_logger
logger.info("setup_logger imported successfully")

logger.info("Importing Webcam from camera.webcam")
from camera.webcam import Webcam
logger.info("Webcam imported successfully")

logger.info("Importing HolisticProcessor from processors.holistic_processor")
from processors.holistic_processor import HolisticProcessor
logger.info("HolisticProcessor imported successfully")

logger.info("Importing WireframeDrawer from visualizers.wireframe_drawer")
from visualizers.wireframe_drawer import WireframeDrawer
logger.info("WireframeDrawer imported successfully")

# logger.info("Importing Recorder from services.recorder")
# from services.recorder import Recorder  # Commented out for now

# -------------------------
# Main Application
# -------------------------
def main():
    logger.info("Starting main() function")

    # -------------------------
    # Load configuration
    # -------------------------
    try:
        logger.info("Loading config/config.yaml")
        config = load_config("config/config.yaml")
        logger.info("Loading config/logging_config.yaml")
        logger_config = load_config("config/logging_config.yaml")
        logger.info("Configuration files loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load config files: {e}")
        return

    # -------------------------
    # Setup logger
    # -------------------------
    log_level_str = logger_config['logger'].get('level', 'INFO').upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger_main = setup_logger(
        name=logger_config['logger'].get('name', 'FullBodyWireframe'),
        log_file=logger_config['logger'].get('log_file', 'logs/app.log'),
        level=log_level
    )
    logger_main.info("Logger initialized successfully")
    logger_main.info("Starting Full Body Wireframe Enterprise Edition")

    # -------------------------
    # Initialize modules
    # -------------------------
    cam = None
    processor = None
    drawer = None
    # recorder = None

    try:
        logger_main.info("Initializing Webcam")
        cam_cfg = config['camera']
        cam = Webcam(camera_id=cam_cfg.get('camera_id', 0), flip=cam_cfg.get('flip', True))
        logger_main.info("Webcam initialized successfully")

        logger_main.info("Initializing HolisticProcessor")
        holistic_cfg = config['holistic']
        processor = HolisticProcessor(
            model_complexity=holistic_cfg.get('model_complexity', 1),
            min_detection_confidence=holistic_cfg.get('min_detection_confidence', 0.5),
            min_tracking_confidence=holistic_cfg.get('min_tracking_confidence', 0.5)
        )
        logger_main.info("HolisticProcessor initialized successfully")

        logger_main.info("Initializing WireframeDrawer")
        drawer = WireframeDrawer()
        logger_main.info("WireframeDrawer initialized successfully")

        # -------------------------
        # Recorder commented out
        # -------------------------
        # logger_main.info("Initializing Recorder")
        # rec_cfg = config['recorder']
        # recorder = Recorder(
        #     output_dir=rec_cfg.get('output_dir', 'recordings'),
        #     filename=rec_cfg.get('filename', 'output.mp4'),
        #     fps=rec_cfg.get('fps', 30)
        # )
        # first_frame = cam.read_frame()
        # recorder.start(first_frame)
        # recorder.write(first_frame)
        # logger_main.info(f"Recorder started at {recorder.filepath} with frame size {recorder.frame_size}")

    except Exception as e:
        logger_main.error(f"Failed to initialize modules: {e}")
        return

    # -------------------------
    # Main loop
    # -------------------------
    frame_counter = 0
    log_interval = 10  # log every 10 frames
    try:
        logger_main.info("Entering main loop")
        while True:
            frame_counter += 1
            frame = cam.read_frame()
            results = processor.process(frame)
            black_image = drawer.draw(frame, results)
            combined_image = cv2.hconcat([frame, black_image])

            # -------------------------
            # Recorder writing commented out
            # -------------------------
            # recorder.write(combined_image)

            # -------------------------
            # Frame logging
            # -------------------------
            if frame_counter % log_interval == 0:
                height, width = frame.shape[:2]
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logger_main.info(f"Frame {frame_counter}: size={width}x{height}, timestamp={timestamp}")

            cv2.imshow("Full Body Wireframe", combined_image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                logger_main.info("Exit key pressed. Closing application.")
                break
    except Exception as e:
        logger_main.error(f"Error during main loop: {e}")
    finally:
        logger_main.info("Starting cleanup of resources...")

        if cam:
            cam.release()
            logger_main.info("Webcam released successfully")

        if processor:
            processor.close()
            logger_main.info("HolisticProcessor closed successfully")

        # if recorder:
        #     recorder.stop()
        #     logger_main.info("Recorder stopped successfully")

        cv2.destroyAllWindows()
        logger_main.info("All OpenCV windows destroyed successfully")

        logger_main.info("Application closed gracefully")

if __name__ == "__main__":
    logger.info("Executing main()")
    main()
