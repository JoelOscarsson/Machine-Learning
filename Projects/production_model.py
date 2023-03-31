import pandas as pd
import joblib

# Load in test data
test_data = pd.read_csv(
    "/Users/joeloscarsson/Documents/www/Machine-Learning/Projects/files/test_samples.csv"
)

# loading in the pkl file
model = joblib.load(
    "/Users/joeloscarsson/Documents/www/Machine-Learning/Projects/model.pkl"
)

# Make predictions on the 100 test samples and export one file  "predictions.csv"
X_test, y_test = test_data.drop("cardio", axis=1), test_data["cardio"]

# predict on test samples
pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# Create a dataframe with the predictions
results = pd.DataFrame({'probability class 0': y_prob[:, 0], 'probability class 1': y_prob[:, 1], 'prediction': pred})

# Save predictions to csv file
results.to_csv("/Users/joeloscarsson/Documents/www/Machine-Learning/Projects/files/predictions.csv", index=False)