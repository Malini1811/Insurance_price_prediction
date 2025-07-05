# 🏥 Insurance Cost Prediction Web App

This is a Flask-based web application that predicts the **medical insurance charges** for individuals based on personal attributes such as age, BMI, number of children, smoking habits, and more. The model was trained using linear regression.

## 🔍 Project Features

- User-friendly web interface to input insurance details
- Machine learning model predicts medical insurance costs
- Pre-trained regression model stored as `regression.pickle`
- Flask backend handles routing and prediction logic
- Modular HTML templates (e.g., form page, result page, thank you page)

## 📁 Project Structure

```
insurance-prediction/
│
├── app.py                    # Flask application
├── regression.pickle         # Trained regression model (pickle format)
├── templates/                # HTML templates for the UI
│   ├── insurance.html
│   ├── insurancepred.html
│   ├── reg_pred.html
│   ├── remdie.html
│   ├── descrption.html
│   └── thanku.html
├── static/                   # (Optional) CSS, JS, image files if any
├── insurance prediction.ipynb  # Notebook used for model training
└── README.md                 # Project documentation
```

## ⚙️ How to Run the Project

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Customer_Transcation.git
cd Customer_Transcation
```

### ✅ 2. Set Up a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, use:

```bash
pip install flask pandas numpy scikit-learn
```

### ✅ 4. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## 📊 Input Features Used for Prediction

- Age
- Sex (encoded)
- BMI
- Number of children
- Smoker (encoded)
- Region (encoded)
- Any other additional fields from your form

## 📦 Model Details

- Model Type: Linear Regression
- Trained using: `insurance prediction.ipynb`
- Saved as: `regression.pickle`

## 💡 Future Improvements

- Add model explainability (e.g., SHAP or LIME)
- Improve model accuracy using ensemble methods
- Secure input validation

