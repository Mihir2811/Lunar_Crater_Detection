# Lunar Crater Detection System

Web-based application for automated detection and analysis of lunar craters using YOLOv8 deep learning model. Developed for Space Applications Centre (SAC), Indian Space Research Organisation (ISRO).

## System Capabilities

- Crater detection from uploaded lunar surface imagery
- Configurable confidence threshold (range: 0.1 to 1.0)
- Annotated output images with bounding box visualization
- JSON format data export for detection results
- Web-based user interface
- Application logging and monitoring

## Technical Specifications

- Backend Framework: Flask (Python)
- Machine Learning Model: YOLOv8 (Ultralytics)
- Image Processing: OpenCV
- Frontend: HTML5, CSS, JavaScript

## System Requirements

- Python 3.7 or higher
- pip package manager

## Installation Procedure

1. Clone repository:
```bash
git clone <repository-url>
cd Lunar_Crater_Detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Model configuration:
   - Place trained model file in Models/ directory
   - Update MODEL_PATH in detect.py as required

## Operation Instructions

### Starting the Application

1. Execute the following command:
```bash
python app.py
```

2. Access the application at:
```
http://localhost:5000
```

### Operating Procedure

1. Upload lunar surface image file
2. Set confidence threshold using slider control
3. Execute analysis by clicking "Analyze Lunar Surface"
4. Review detection results with bounding box annotations
5. Download annotated image and JSON data as required

### Supported File Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- Maximum file size: 10MB

## Directory Structure

```
Lunar_Crater_Detection/
├── Models/                 # Trained model files
│   ├── yolov8_model.pt    # Primary trained model
│   └── yolov8n.pt         # Base YOLOv8 model
├── static/                # Output files
├── templates/             # HTML templates
│   └── index.html         # Web interface
├── uploads/               # User uploaded images
├── app.py                 # Flask application
├── detect.py              # Detection module
├── requirements.txt       # Dependencies
├── .gitignore            # Git configuration
└── README.md             # Documentation
```

## API Specification

### GET /
- Description: Main application interface
- Returns: HTML page

### POST /upload
- Description: Image processing endpoint
- Parameters:
  - image: Image file (multipart/form-data)
  - confidence: Threshold value (0.1-1.0)
- Returns: HTML page with results

## Output Specification

### Annotated Image
- Input image with bounding boxes indicating detected craters
- Confidence scores for each detection
- Saved in static/ directory

### JSON Data
Detailed detection information:
```json
{
    "image_path": "path/to/uploaded/image.jpg",
    "model": "Models/yolov8_model.pt",
    "confidence_threshold": 0.5,
    "detections": [
        {
            "class_id": 0,
            "class_name": "crater",
            "confidence": 0.85,
            "bbox": {
                "x1": 100,
                "y1": 150,
                "x2": 200,
                "y2": 250
            }
        }
    ]
}
```

## Configuration Parameters

### Model Settings
- MODEL_PATH in detect.py: Specify model file location
- box_thickness: Bounding box line width

### Logging Settings
- Log file: app.log
- Logging levels: DEBUG, INFO, WARNING, ERROR (configurable in app.py)

## Development Guidelines

### Modification Procedures
1. Backend modifications: app.py or detect.py
2. Frontend modifications: templates/index.html
3. Styling modifications: CSS classes in HTML template

### Custom Model Integration
1. Train YOLOv8 model on lunar crater dataset
2. Save model as .pt file in Models/ directory
3. Update MODEL_PATH in detect.py

## Troubleshooting

### Common Issues

1. Model not found: Verify model file exists in Models/ directory
2. Upload failure: Verify file size (maximum 10MB) and format (JPG/PNG)
3. Detection errors: Verify image quality and adjust confidence threshold
4. Port conflicts: Modify port number in app.run() if port 5000 is unavailable

### Log Files
Refer to app.log for error messages and application status.

## Performance Notes

- Image Size: Processing time increases with image dimensions
- Confidence Threshold: Lower values increase detection count and false positive rate
- Model Size: Larger models improve accuracy with increased processing time

## License

Developed for Space Applications Centre (SAC), Indian Space Research Organisation (ISRO). Refer to organizational licensing terms.

## Author

Mihir Panchal

## Acknowledgments

- Space Applications Centre (SAC), ISRO
- Ultralytics YOLOv8 framework
- OpenCV library
- Flask framework