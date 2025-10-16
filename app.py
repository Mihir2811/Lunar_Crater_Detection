import os
import logging
from flask import Flask, render_template, request, redirect
from detect import detect_image

# -----------------------------
# Flask App Setup
# -----------------------------
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# -----------------------------
# Logging Configuration
# -----------------------------
LOG_FILE = "app.log"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Change to INFO in production

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] in %(module)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# -----------------------------
# Routes
# -----------------------------
@app.route('/', methods=['GET'])
def index():
    logger.info("Homepage accessed.")
    return render_template('index.html', image_path=None, json_path=None)


@app.route('/upload', methods=['POST'])
def upload():
    """Handle image upload and detection."""
    if 'image' not in request.files:
        logger.warning("Upload request without an image file.")
        return redirect('/')

    file = request.files['image']
    conf = float(request.form.get('confidence', 0.5))  # Confidence slider value

    if file.filename == '':
        logger.warning("Upload request with empty filename.")
        return redirect('/')

    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        logger.info(f"File uploaded: {filepath} (conf={conf})")

        # Run detection
        output_img, output_json = detect_image(filepath, conf, box_thickness=1)
        logger.info(f"Detection finished. Image: {output_img}, JSON: {output_json}")

        cache_buster = os.urandom(4).hex()
        return render_template(
            'index.html',
            image_path=f"{output_img}?{cache_buster}",
            json_path=output_json
        )

    except Exception as e:
        logger.exception(f"Error during processing: {e}")
        return "Detection failed. Check logs.", 500


@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 - {error}")
    return "404 - Page not found", 404


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 - Internal Server Error: {error}")
    return "500 - Internal Server Error", 500


if __name__ == '__main__':
    logger.info("Starting Lunar Crater Detection Flask server...")
    try:
        app.run(debug=True)
    except Exception as e:
        logger.exception(f"Flask crashed: {e}")
