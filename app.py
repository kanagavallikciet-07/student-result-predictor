from flask import Flask, request, render_template_string
import joblib
import os

app = Flask(__name__)
model = joblib.load("student_model.pkl")
VERSION = os.getenv("MODEL_VERSION", "1.0")

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Predictor</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            text-align: center;
            padding: 40px;
        }
        .box {
            background: white;
            max-width: 420px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
        }
        input, button {
            width: 90%;
            padding: 12px;
            margin: 10px;
            box-sizing: border-box;
        }
        button {
            background: #1769aa;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>Student Result Predictor</h1>
        <p>Model Version: {{ version }}</p>
        <form method="POST">
            <input type="number" name="hours"
                   placeholder="Study Hours" min="0" max="24"
                   step="0.5" required>
            <input type="number" name="attendance"
                   placeholder="Attendance %" min="0" max="100"
                   required>
            <input type="number" name="marks"
                   placeholder="Internal Marks" min="0" max="100"
                   required>
            <button type="submit">Predict Result</button>
        </form>
        {% if result %}
            <h2>Prediction: {{ result }}</h2>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = int(request.form["attendance"])
        marks = int(request.form["marks"])
        result = model.predict([[hours, attendance, marks]])[0]

    return render_template_string(
        PAGE, version=VERSION, result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
