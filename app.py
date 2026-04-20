import os
import numpy as np
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# -----------------------------------
# FLASK SETUP
# -----------------------------------
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# -----------------------------------
# LOAD MODEL
# -----------------------------------
model = load_model("model.h5")

with open("requirements.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# -----------------------------------
# HAIR CONDITIONS DATABASE (DETAILED)
# -----------------------------------
HAIR_CONDITIONS = {

    'Dandruff': {
        'description': 'White flakes on scalp and hair',
        'causes': [
            'Dry scalp',
            'Malassezia fungus overgrowth',
            'Poor hygiene',
            'Stress and hormonal imbalance'
        ],
        'precautions': [
            'Use anti-dandruff shampoo containing zinc pyrithione or ketoconazole',
            'Wash hair regularly (every alternate day)',
            'Avoid tight hairstyles',
            'Manage stress through exercise and meditation',
            'Maintain proper diet with omega-3 fatty acids',
            'Avoid harsh chemical treatments'
        ],
        'treatment': [
            'Apply medicated shampoo for 2-3 weeks',
            'Use scalp moisturizer or oil',
            'Consult dermatologist if persistent'
        ]
    },

    'Hair Loss': {
        'description': 'Excessive hair shedding',
        'causes': [
            'Genetics (androgenetic alopecia)',
            'Hormonal imbalance',
            'Nutritional deficiency',
            'Stress and anxiety'
        ],
        'precautions': [
            'Avoid tight braiding',
            'Minimize heat styling',
            'Eat protein-rich foods',
            'Massage scalp regularly'
        ],
        'treatment': [
            'Consult dermatologist',
            'Minoxidil treatment',
            'Hair growth supplements'
        ]
    },

    'Alopecia Areata': {
        'description': 'Patchy hair loss in circular areas',
        'causes': [
            'Autoimmune condition',
            'Genetic predisposition',
            'Severe stress'
        ],
        'precautions': [
            'Manage stress',
            'Avoid pulling hair',
            'Gentle hair care'
        ],
        'treatment': [
            'Topical corticosteroids',
            'Minoxidil',
            'Immunotherapy'
        ]
    }
}

# -----------------------------------
# FORMAT LIST FUNCTION
# -----------------------------------
def format_list(items):
    return "\n".join([f"• {item}" for item in items])

# -----------------------------------
# HOME ROUTE
# -----------------------------------
@app.route('/')
def home():
    return render_template("index.html")

# -----------------------------------
# PREDICT ROUTE
# -----------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']

    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Preprocess image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)
    confidence_score = round(float(np.max(predictions)) * 100, 2)
    predicted_class = class_names[np.argmax(predictions)]

    # Match safely
    info = HAIR_CONDITIONS.get(predicted_class)

    if info:
        explanation = f"""
🧠 AI Medical Analysis Report

Condition: {predicted_class}
Confidence: {confidence_score}%

📖 Description:
{info['description']}

⚠ Causes:
{format_list(info['causes'])}

🛡 Precautions:
{format_list(info['precautions'])}

💊 Treatment:
{format_list(info['treatment'])}
"""
    else:
        explanation = "Information not available. Please consult a dermatologist."

    return render_template(
        "result.html",
        result=predicted_class,
        confidence=confidence_score,
        image_path=filepath,
        explanation=explanation
    )

# -----------------------------------
# CHAT ROUTE
# -----------------------------------
@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json["message"].lower()
    response = "Please consult a dermatologist for accurate medical advice."

    for disease, info in HAIR_CONDITIONS.items():
        if disease.lower() in user_message:
            response = f"""
🧠 AI Assistant Response

Condition: {disease}

Description:
{info['description']}

Treatment:
{format_list(info['treatment'])}

Precautions:
{format_list(info['precautions'])}
"""
            break

    return jsonify({"reply": response})

# -----------------------------------
# RUN APP
# -----------------------------------
if __name__ == "__main__":
    app.run(debug=True)