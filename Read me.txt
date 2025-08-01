# 🩺 Diabetes Prediction System

A machine learning web application built with Flask that predicts whether a person is diabetic or not based on medical input data. It uses the **Random Forest Classifier** trained on the **PIMA Indians Diabetes Dataset**.

---

## 🚀 Features

- 📊 Predicts diabetic/non-diabetic status from input features
- 💻 Simple and user-friendly web interface (HTML + CSS)
- 🔄 Preprocessing includes:
  - Handling zero/impossible values
  - Feature scaling using MinMaxScaler
  - Handling class imbalance using SMOTE
- 🧠 Model trained using RandomForestClassifier

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML/CSS
- Scikit-learn
- NumPy / Pandas
- imbalanced-learn (SMOTE)

---

## 📥 Input Features

| Feature                  | Expected Range         |
|--------------------------|------------------------|
| Pregnancies              | 0 - 17                 |
| Glucose Level            | 70 - 200               |
| Blood Pressure           | 40 - 130               |
| Skin Thickness           | 10 - 99                |
| Insulin Level            | 15 - 846               |
| BMI                      | 15 - 67                |
| Diabetes Pedigree Func.  | 0.05 - 2.5             |
| Age                      | 21 - 81                |

---

## 💡 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows


3. Install dependencies

bash
Copy
Edit
pip install -r requirements.txt


4. Run the app

bash
Copy
Edit
python app.py


5. Visit http://127.0.0.1:5000/ in your browser.



Project Structure
├── app.py
├── model.pkl
├── scaler.pkl
├── templates/
│   ├── index.html
│   └── form.html
├── static/
│   └── (optional: your CSS/JS/images)
├── requirements.txt
└── README.md

For any questions or suggestions:
Fahad Akram
ppbizon56t@gmail.com
