def predict(data):
    import joblib
    import pickle
    import pandas as pd


    data = pd.read_csv('test.csv')
    categ = data['Scholarship holder']
    columns_to_drop = [
        'id', 'Marital status', 'Application mode', 'Application order', 'Course',
        'Daytime/evening attendance', 'Previous qualification', 'Nacionality',
        'Displaced', 'Educational special needs', 'Debtor', 'Gender',
        'International', 'Curricular units 1st sem (credited)',
        'Curricular units 1st sem (without evaluations)',
        'Curricular units 2nd sem (credited)',
        'Curricular units 2nd sem (without evaluations)', 'Scholarship holder'
    ]
    new_data = data.drop(columns=columns_to_drop, axis='columns')
    scaled_model = joblib.load('scaler.joblib')
    new_data = new_data[scaled_model.feature_names_in_]
    scaled = scaled_model.transform(new_data)
    scaled_df = pd.DataFrame(data=scaled, columns=new_data.columns)
    scaled_df['Scholarship holder'] = categ.reset_index(drop=True)
    with open('rf.pkl', 'rb') as file:
        model = pickle.load(file)


    predictions = model.predict(scaled_df)
    predictions = pd.DataFrame(data=predictions, columns=['Target'])
    pred_data = pd.concat([data, predictions], axis='columns')
    pred_data['Target']=pred_data['Target'].replace({'0':'Graduate','1':'Enrolled','2':'Dropout'})
    pred_data.to_excel('predictions.xlsx', index=False)