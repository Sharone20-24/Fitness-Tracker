import joblib
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from utils.preprocessing import load_and_merge_data, prepare_features_and_labels

# Load and preprocess data
data = load_and_merge_data('data/exercise.csv', 'data/calories.csv')
X, y = prepare_features_and_labels(data)

# Train classifier (you can define custom categories if needed)
classifier = RandomForestClassifier()
classifier.fit(X, y > y.median())  # Classify above/below median calories burned

# Train regressor for calorie prediction
regressor = RandomForestRegressor()
regressor.fit(X, y)

# Save models
joblib.dump(classifier, 'models/classifier.pkl')
joblib.dump(regressor, 'models/regressor.pkl')

print("✅ Models trained and saved successfully!")
