from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Allow cross-origin requests

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image']
    path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(path)

    # Read and process the image
    img = cv2.imread(path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    green_pixels = cv2.countNonZero(green_mask)
    total_pixels = img.shape[0] * img.shape[1]
    percent_green = round((green_pixels / total_pixels) * 100, 2)

    return jsonify({"green_coverage_percent": percent_green})

if __name__ == '__main__':
    app.run(debug=True)