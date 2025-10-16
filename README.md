# Lunar Crater Detection

A web-based application that uses YOLOv8 deep learning model to detect and analyze lunar craters in uploaded images. Built for SAC, ISRO.

## Features

- **Real-time Crater Detection**: Upload lunar surface images and get instant crater detection results
- **Adjustable Confidence Threshold**: Fine-tune detection sensitivity with a slider (0.1 to 1.0)
- **Visual Results**: View annotated images with detected craters highlighted in bounding boxes
- **Data Export**: Download processed images and detection data in JSON format
- **Modern Web Interface**: Responsive design with interactive 3D background
- **Comprehensive Logging**: Detailed application logs for monitoring and debugging

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **3D Graphics**: Vanta.js for interactive background
- **Icons**: Feather Icons

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Lunar_Crater_Detection
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have the trained YOLOv8 model:
   - Place your trained model file in the `Models/` directory
   - Update the `MODEL_PATH` in `detect.py` if using a different model name

## Usage

### Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

### Using the Web Interface

1. **Upload Image**: Click the upload area or drag and drop a lunar surface image
2. **Adjust Sensitivity**: Use the confidence slider to set detection threshold
3. **Analyze**: Click "Analyze Lunar Surface" to process the image
4. **View Results**: See detected craters highlighted with bounding boxes
5. **Download**: Save the annotated image and JSON detection data

### Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- Maximum file size: 10MB

## Project Structure

```
Lunar_Crater_Detection/
├── Models/                 # Trained YOLOv8 models
│   ├── yolov8_model.pt    # Main trained model
│   └── yolov8n.pt         # Base YOLOv8 nano model
├── static/                # Generated output files
├── templates/             # HTML templates
│   └── index.html         # Main web interface
├── uploads/               # Uploaded user images
├── app.py                 # Flask web application
├── detect.py              # YOLOv8 detection logic
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## API Endpoints

### GET /
- **Description**: Main application page
- **Returns**: HTML interface for image upload

### POST /upload
- **Description**: Process uploaded image for crater detection
- **Parameters**:
  - `image`: Image file (multipart/form-data)
  - `confidence`: Detection confidence threshold (0.1-1.0)
- **Returns**: HTML page with detection results

## Detection Output

### Annotated Image
- Original image with green bounding boxes around detected craters
- Confidence scores displayed for each detection
- Saved in `static/` directory with unique filename

### JSON Data
Contains detailed detection information:
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

## Configuration

### Model Configuration
- Update `MODEL_PATH` in `detect.py` to use different trained models
- Adjust `box_thickness` parameter for bounding box appearance

### Logging Configuration
- Logs are saved to `app.log`
- Adjust logging levels in `app.py` (DEBUG, INFO, WARNING, ERROR)

## Development

### Adding New Features
1. Backend logic: Modify `app.py` or `detect.py`
2. Frontend changes: Update `templates/index.html`
3. Styling: Modify Tailwind CSS classes in the HTML template

### Model Training
To use a custom trained model:
1. Train your YOLOv8 model on lunar crater dataset
2. Save the model as `.pt` file in `Models/` directory
3. Update `MODEL_PATH` in `detect.py`

## Troubleshooting

### Common Issues

1. **Model not found**: Ensure the model file exists in the `Models/` directory
2. **Upload fails**: Check file size (max 10MB) and format (JPG/PNG)
3. **Detection errors**: Verify image quality and adjust confidence threshold
4. **Port conflicts**: Change the port in `app.run()` if 5000 is occupied

### Logs
Check `app.log` for detailed error messages and application behavior.

## Performance Considerations

- **Image Size**: Larger images take longer to process
- **Confidence Threshold**: Lower values detect more objects but may include false positives
- **Model Size**: Larger models provide better accuracy but slower inference

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is developed for SAC, ISRO. Please refer to the organization's licensing terms.

## Author

**Mihir Panchal**  
Developed for Space Applications Centre (SAC), ISRO

## Acknowledgments

- ISRO Space Applications Centre for project guidance
- Ultralytics for YOLOv8 framework
- OpenCV community for computer vision tools
- Flask development team for the web framework