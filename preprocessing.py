import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_merge_data(exercise_path, calories_path):
    # Load the CSV files
    exercise_data = pd.read_csv(exercise_path)
    calories_data = pd.read_csv(calories_path)

    # Merge both datasets on User_ID
    merged_data = pd.merge(exercise_data, calories_data, on="User_ID")

    # Encode categorical data (Gender)
    label_encoder = LabelEncoder()
    merged_data['Gender'] = label_encoder.fit_transform(merged_data['Gender'])

    # Handle missing values
    merged_data.fillna(merged_data.mean(), inplace=True)

    # Normalize numerical features
    scaler = StandardScaler()
    numeric_features = ['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
    merged_data[numeric_features] = scaler.fit_transform(merged_data[numeric_features])

    return merged_data

def prepare_features_and_labels(data):
    X = data.drop(['User_ID', 'Calories'], axis=1)
    y = data['Calories']
    return X, y
