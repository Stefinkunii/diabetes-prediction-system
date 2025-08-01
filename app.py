from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get and process input values
        inputs = [float(request.form[key]) for key in request.form]
        final_input = np.array([inputs])

        # Apply scaling
        scaled_input = scaler.transform(final_input)

        # Make prediction
        prediction = model.predict(scaled_input)
        output = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

        return render_template('form.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
