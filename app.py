from flask import Flask, request, jsonify, render_template
import joblib
import pickle
import pandas as pd
import time

app = Flask(__name__)

class AcademicSuccess:
    def __init__(self, scaler_path, model_path):
        self.scaler = joblib.load(scaler_path)
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)

        self.feature_names = [
            'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)',
            'Curricular units 1st sem (grade)', 'Curricular units 1st sem (approved)',
            'Curricular units 2nd sem (evaluations)', 'Curricular units 1st sem (evaluations)',
            'Admission grade', 'Previous qualification (grade)', 'Age at enrollment',
            'Tuition fees up to date', "Father's occupation", 'Course', "Mother's occupation",
            'GDP', 'Unemployment rate', 'Scholarship holder', "Mother's qualification",
            "Father's qualification", 'Inflation rate', 'Application mode',
            'Curricular units 2nd sem (enrolled)', 'Application order',
            'Curricular units 1st sem (enrolled)', 'Gender', 'Debtor', 'Displaced',
            'Previous qualification', 'Curricular units 1st sem (credited)', 'Marital status',
            'Curricular units 2nd sem (without evaluations)',
            'Curricular units 1st sem (without evaluations)',
            'Curricular units 2nd sem (credited)', 'Daytime/evening attendance',
            'Nacionality', 'Educational special needs', 'International'
        ]

    def predict(self, input_data):
        input_df = pd.DataFrame([input_data])
        aligned_df = pd.DataFrame(columns=self.feature_names)
        for col in self.feature_names:
            aligned_df[col] = input_df.get(col, 0)
        scaled_data = self.scaler.transform(aligned_df)
        prediction = self.model.predict(scaled_data)

        label_mapping = {0: 'Graduate', 1: 'Enrolled', 2: 'Dropout'}
        return label_mapping.get(prediction[0], "Unknown")

academic_success = AcademicSuccess(
    scaler_path='D:/Environments/Projects/Academic-Success-Classification/experiments/scaler.joblib',
    model_path='D:/Environments/Projects/Academic-Success-Classification/experiments/rf.pkl'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    input_data = request.json
    try:
        prediction = academic_success.predict(input_data)
        time.sleep(2)

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)