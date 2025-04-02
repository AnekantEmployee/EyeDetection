import io
from PIL import Image
from .eye_detection import EyeDetector
from flask import Flask, request, jsonify


app = Flask(__name__)
eye_detector = EyeDetector()


@app.route("/detect_eye_state", methods=["POST"])
def detect_eye_state():
    """
    Endpoint to detect the eye state from an uploaded image.
    """
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_file = request.files["image"]

    try:
        image_pil = Image.open(io.BytesIO(image_file.read()))
        eye_state = eye_detector.get_eye_state(image_pil)
        return jsonify(eye_state)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)  # remove debug=True for production
