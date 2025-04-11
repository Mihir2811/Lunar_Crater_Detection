from ultralytics import YOLO
import cv2

model = YOLO("yolov8_model.pt")  # replace with your model if needed

def detect_image(image_path):
    results = model(image_path)
    result_img = results[0].plot()

    output_path = "static/output.jpg"
    cv2.imwrite(output_path, result_img)
