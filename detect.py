from ultralytics import YOLO
import cv2
import os
import uuid
import json
import logging

# -----------------------------
# YOLO Model Initialization
# -----------------------------
MODEL_PATH = "Models/yolov8_model.pt"  # Replace with your trained model
model = YOLO(MODEL_PATH)

# -----------------------------
# Logging Setup
# -----------------------------
logger = logging.getLogger(__name__)

# -----------------------------
# Detection Function
# -----------------------------
def detect_image(image_path, conf=0.5, box_thickness=1):
    """
    Runs YOLOv8 detection on an image.
    Saves:
      - Annotated image (in static/)
      - JSON file with detection data
    Returns:
      (output_image_path, output_json_path)
    """
    try:
        logger.info(f"Running YOLOv8 detection on {image_path} (conf={conf})")

        # Run inference
        results = model(image_path, conf=conf)
        boxes = results[0].boxes.xyxy.cpu().numpy()  # [x1, y1, x2, y2]
        confs = results[0].boxes.conf.cpu().numpy()  # confidence scores
        cls_ids = results[0].boxes.cls.cpu().numpy()  # class indices
        names = model.names  # class names

        # Read input image
        img = cv2.imread(image_path)
        detections = []

        # Draw boxes and store detection data
        for (box, score, cls_id) in zip(boxes, confs, cls_ids):
            x1, y1, x2, y2 = map(int, box)
            label = names[int(cls_id)]
            color = (0, 255, 0)  # Green for craters

            # Draw thin bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), color, box_thickness)
            cv2.putText(
                img, f"{label} {score:.2f}",
                (x1, max(y1 - 8, 15)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA
            )

            # Append to JSON data
            detections.append({
                "class_id": int(cls_id),
                "class_name": label,
                "confidence": float(score),
                "bbox": {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
            })

        # Ensure output folder exists
        os.makedirs("static", exist_ok=True)
        unique_id = uuid.uuid4().hex
        output_image_path = os.path.join("static", f"{unique_id}.jpg")
        output_json_path = os.path.join("static", f"{unique_id}.json")

        # Save image
        cv2.imwrite(output_image_path, img)

        # Save JSON
        with open(output_json_path, "w") as f:
            json.dump({
                "image_path": image_path,
                "model": MODEL_PATH,
                "confidence_threshold": conf,
                "detections": detections
            }, f, indent=4)

        logger.info(f"Detection complete → Image: {output_image_path}, JSON: {output_json_path}")
        return output_image_path, output_json_path

    except Exception as e:
        logger.exception(f"Detection failed: {e}")
        raise
