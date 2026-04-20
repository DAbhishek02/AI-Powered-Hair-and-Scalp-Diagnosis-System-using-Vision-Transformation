🚀 AI-Powered Hair & Scalp Diagnosis System
📌 Project Summary
The AI-Powered Hair and Scalp Diagnosis System (AI-HSDS) is a deep learning–based application designed to automatically detect and classify hair and scalp conditions using medical images.
Traditional diagnosis is subjective and depends on dermatologists. This system uses Vision Transformer (ViT) and MobileNetV2 to provide:
Fast and accurate diagnosis
Multi-class classification (14 conditions)
Personalized recommendations
It also integrates image processing + AI + user guidance, making it useful for both individual users and healthcare support.

🎯 Objectives
Build an AI model for scalp disease classification
Detect 14 different hair/scalp conditions
Improve accuracy using Vision Transformers
Provide personalized care recommendations
Create a user-friendly interface (Gradio)
🧠 Model Architecture
🔹 Hybrid Approach:
MobileNetV2 (Transfer Learning) → Efficient feature extraction
Vision Transformer (ViT) → Global pattern understanding
🔹 Pipeline:
Input Image
Preprocessing
Feature Extraction
Classification
Recommendation Engine
📊 Dataset Details
Source: Kaggle (Hair & Scalp Disease Dataset)
Total Classes: 14
Includes:
Alopecia Areata
Dandruff
Folliculitis
Psoriasis
Telogen Effluvium
etc.
📌 Dataset Features:
Diverse skin types
Different lighting conditions
Dermoscopic & normal images
Balanced + imbalanced classes
⚙️ Dataset Processing
1. Data Cleaning
Remove corrupted images
Verify labels
2. Preprocessing
Resize → 224 × 224
Normalize pixel values [0,1]
Apply CLAHE (contrast enhancement)
3. Data Augmentation
Rotation (±20°)
Flipping
Brightness adjustment
4. Dataset Split
Training → 70%
Validation → 15%
Testing → 15%
🧪 Model Training
🔹 Loss Function
Categorical Cross Entropy
🔹 Optimizer
Adam (lr = 0.001)
🔹 Techniques Used
Early Stopping
Learning Rate Scheduler
Class Weights (for imbalance)
📈 Evaluation Metrics
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
🔄 Workflow (Step-by-Step)
Step 1: Data Collection
Download dataset from Kaggle
Step 2: Preprocessing
Resize, normalize, enhance
Step 3: Model Building
Load MobileNetV2 (pretrained)
Add custom layers
(Optional) Integrate ViT
Step 4: Training
Train on dataset
Validate performance
Step 5: Evaluation
Generate confusion matrix
Analyze metrics
Step 6: Deployment
Build UI using Gradio
Upload image → Get diagnosis
💡 Features

✅ Multi-class classification (14 diseases)
✅ AI-based scalp analysis
✅ Personalized recommendations
✅ Lightweight + scalable
✅ Works with normal images

🖥️ Tech Stack
Python
TensorFlow / Keras
OpenCV
NumPy
Matplotlib
Gradio
📦 Installation
git clone https://github.com/your-username/hair-scalp-diagnosis.git
cd hair-scalp-diagnosis
pip install -r requirements.txt
▶️ Run the Project
python app/app.py
📊 Future Improvements
Improve accuracy (current ~46%)
Add more dataset samples
Use advanced models (Swin Transformer)
Mobile app integration
Real-time camera diagnosis
