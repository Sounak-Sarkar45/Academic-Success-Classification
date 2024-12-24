import joblib
import pickle
import pandas as pd

class AcademicSuccess:
    def __init__(self,
                 scaler_path='scaler.joblib', 
                 model_path='rf.pkl'):
        # Load the scaler and model
        self.scaled_model = joblib.load(scaler_path)
        with open(model_path, 'rb') as file:
            self.model = pickle.load(file)
        
        # Store feature names that were used during model training
        self.feature_names = self.scaled_model.feature_names_in_

    def predict_to_xlsx(self, data, output_path='Predictions.xlsx'):
        # Preserve the id in a separate dataframe
        id = data['id']
        
        # Now drop the ID column
        data = data.drop('id', axis='columns')
        
        # Ensure columns are aligned with the original model training set
        missing_cols = set(self.feature_names) - set(data.columns)
        extra_cols = set(data.columns) - set(self.feature_names)
        
        # If there are missing columns, add them with default values (e.g., 0)
        for col in missing_cols:
            data[col] = 0  # Or use any default value suitable for your use case
        
        # If there are extra columns, drop them
        data = data[[col for col in self.feature_names if col in data.columns]]
        
        # Reorder columns to match the order used during training
        data = data[self.feature_names]
        
        # Scale the data using the loaded scaler
        scaled_data = self.scaled_model.transform(data)
        
        # Initialize a DataFrame to store the predictions
        prediction = pd.DataFrame()
        prediction['Target'] = self.model.predict(scaled_data)
        
        # Merge the id and predictions
        prediction_data = pd.concat([id, data ,prediction], axis='columns')
        
        # Rename the predictions
        prediction_data.Target = prediction_data.Target.replace({0: 'Graduate', 1: 'Enrolled', 2: 'Dropout'})
        
        # Save the predictions to an Excel file
        prediction_data.to_excel(output_path, index=False)
    
    def predict(self, data):
        
        # Ensure columns are aligned with the original model training set
        missing_cols = set(self.feature_names) - set(data.columns)
        extra_cols = set(data.columns) - set(self.feature_names)
        
        # If there are missing columns, add them with default values (e.g., 0)
        for col in missing_cols:
            data[col] = 0  # Or use any default value suitable for your use case
        
        # If there are extra columns, drop them
        data = data[[col for col in self.feature_names if col in data.columns]]
        
        # Reorder columns to match the order used during training
        data = data[self.feature_names]
        
        # Scale the data using the loaded scaler
        scaled_data = self.scaled_model.transform(data)
        
        # Make the predictions
        predictions = self.model.predict(scaled_data)
        
        # Return predictions
        return predictions