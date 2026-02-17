from flask import Flask, render_template, request, send_from_directory, url_for
import os
from predict import predict_image

app = Flask(__name__)

# Folder where uploaded images are stored (in project root, not inside static)
UPLOAD_FOLDER = os.path.join(app.root_path, "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    # templates/index.html
    return render_template("index.html")


@app.route("/about")
def about():
    # you can change these values to your real metrics
    accuracy = 94.6
    classes = 4
    dataset_size = 3200

    return render_template(
        "about.html",
        accuracy=accuracy,
        classes=classes,
        dataset_size=dataset_size,
    )


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # 1. Get file
        file = request.files.get("file")
        if not file or file.filename == "":
            return render_template("predict.html", error="Please upload an image.")

        # 2. Save file into uploads/ folder
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # 3. Run model prediction
        label, confidence = predict_image(filepath)

        # 4. Build URL for the image so HTML can display it
        image_url = url_for("uploaded_file", filename=file.filename)  # /uploads/<filename>[web:20]

        # 5. Render result page
        return render_template(
            "result.html",
            prediction_label=label,
            confidence=f"{confidence:.2f}",
            model_name="Transfer Learning CNN",
            image_path=image_url,
        )

    # GET -> show upload form
    return render_template("predict.html")


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    # serves the uploaded file when <img src="{{ image_path }}"> is used[web:17][web:20]
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
