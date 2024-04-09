def calculate_bmi(height, weight):

    # Calculate BMI
    bmi = ((weight * 0.45) / ((height * 0.025) * (height * 0.025)))

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

# app.py
from flask import Flask, render_template, request
from bmi_calculator import calculate_bmi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi, category = calculate_bmi(height, weight)
    return render_template('result.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
