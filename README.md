🍎 Smart Sorting
Transfer Learning for Identifying Rotten Fruits and Vegetables
📌 Project Overview
Smart Sorting is a Deep Learning based web application that classifies fruits and vegetables as Fresh or Rotten using Transfer Learning.
The system is built using:
🧠 TensorFlow & Keras
📷 MobileNetV2 (Pre-trained CNN)
🌐 Flask Web Framework
🎨 HTML, CSS
💻 VS Code
The model is trained on labeled fruit images and integrated into a Flask web application where users can upload an image and receive an instant prediction with confidence score.
📂 Project Structure
<img width="826" height="1018" alt="Screenshot 2026-02-16 201800" src="https://github.com/user-attachments/assets/00300d46-4e48-4174-a8f1-33820cff6adf" />
🌐 Web Application Pages




🏠 1️⃣ Home Page (index.html)
📍 Route:
@app.route("/")
🎯 Purpose:
Introduces the Smart Sorting system
Displays project title and description
Contains navigation menu
Provides “Start Prediction” button
🖼 Screenshot:<img width="1919" height="1024" alt="Screenshot 2026-02-16 121713" src="https://github.com/user-attachments/assets/42dbb6fe-1cbf-4e73-ba66-22fe2421f909" />
📝 Description:
The Home page presents the system as an AI-powered fruit sorting application.
It highlights:
Transfer Learning usage
Real-time prediction capability
Reduced food waste concept
This page acts as the entry point of the application.








📊 2️⃣ About Page (about.html)
📍 Route
@app.route("/about")
🎯 Purpose:
Displays project metrics and model performance.
🖼 Screenshot:<img width="1919" height="1016" alt="Screenshot 2026-02-16 121729" src="https://github.com/user-attachments/assets/502be140-9922-43b3-963e-85aaa385a102" />
📝 Description:
The About page provides detailed information about:
Model Accuracy: 94.6%
Number of Classes: 4
Dataset Size: 3200 Images
24/7 Monitoring capability
This page explains how Transfer Learning with MobileNetV2 is used to achieve high accuracy.








📤 3️⃣ Predict Page (predict.html)
📍 Route:
@app.route("/predict", methods=["GET", "POST"])
🎯 Purpose:
Allows user to upload fruit/vegetable image.
🖼 Screenshot:<img width="1919" height="1016" alt="Screenshot 2026-02-16 121747" src="https://github.com/user-attachments/assets/76f752f1-16da-4ca3-9e06-028be881480b" />

📝 Description:
This page contains:
<form action="/predict" method="POST" enctype="multipart/form-data">

Important features:
File upload option
POST method for secure data transfer
Image preview
“Predict Freshness” button
When the image is uploaded, it is saved into the uploads/ folder.







📈 4️⃣ Result Page (result.html)
📍 Triggered after prediction
🎯 Purpose:
Displays:
Uploaded image
Prediction result (Fresh / Rotten)
Confidence percentage
Model name
🖼 Screenshot:<img width="1915" height="1024" alt="Screenshot 2026-02-16 210258" src="https://github.com/user-attachments/assets/a638ff21-873b-4432-a352-e9df388cb136" />
<img width="1911" height="1019" alt="Screenshot 2026-02-16 121810" src="https://github.com/user-attachments/assets/a7bceb2a-afe3-4378-8345-003b7b0eac03" />

📝 Description:
After image upload:
Image is passed to predict.py
Model predicts probability
Flask renders result page with:
prediction_label
confidence
model_name
image_path
Example Output:
Prediction: Rotten
Confidence: 100%
Model: Transfer Learning CNN






📞 5️⃣ Contact Page (contact.html)
📍 Route:
@app.route("/contact")
🎯 Purpose:
Displays developer and project information.
screenshot:<img width="1919" height="1017" alt="Screenshot 2026-02-16 121931" src="https://github.com/user-attachments/assets/3e57b603-f8ef-4f35-9057-1d7caebc9394" />

📝 Description:
Contains:
Project name
Developer name
Email
Institution details
🧠 Model Building (train.py)
Base Model: MobileNetV2 (ImageNet weights)
Input Size: 224x224
Layers Added:
Flatten
Dense (128, ReLU)
Dropout (0.5)
Output (Sigmoid)
Compilation:
model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["accuracy"])
Accuracy Achieved:
~94%
Model saved as:
model/healthy_vs_rotten.h5
🔍 Prediction Logic (predict.py)
Steps:
Load model
Resize image (224x224)
Normalize pixel values
Expand dimensions
Predict
Return label + confidence
🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Run Flask App
python app.py
3️⃣ Open Browser
http://127.0.0.1:5000
<img width="1904" height="1020" alt="Screenshot 2026-02-16 210205" src="https://github.com/user-attachments/assets/2ae50c8b-1784-41a9-b1dd-e315b212621a" />


📌 Features
✔ Transfer Learning using MobileNetV2
✔ High Accuracy (94%+)
✔ Real-time image prediction
✔ Clean UI
✔ Flask Backend Integration
✔ Easy Deployment
🌍 Real-World Applications
Supermarkets
Warehouses
Agricultural Industry
Food Quality Inspection
Cold Storage Monitoring
📎 Future Enhancements
Multi-class fruit classification
Live camera detection
Deployment on cloud (Heroku / AWS)
Mobile application integration
