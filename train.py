# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import mean_squared_error
# from xgboost import XGBRegressor
# import joblib

# # Load dataset
# df = pd.read_csv("House Price India.csv")

# # Clean column names (remove spaces issues)
# df.columns = df.columns.str.strip()

# print("Columns in dataset:\n", df.columns)

# # Target variable
# y = df['Price']

# # Features
# X = df.drop(['Price'], axis=1)

# # Handle missing values
# for col in X.columns:
#     if X[col].dtype == 'object':
#         X[col] = X[col].fillna(X[col].mode()[0])
#     else:
#         X[col] = X[col].fillna(X[col].median())

# # Encode categorical columns
# le = LabelEncoder()
# for col in X.select_dtypes(include=['object']).columns:
#     X[col] = le.fit_transform(X[col])

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Train model
# model = XGBRegressor(
#     n_estimators=300,
#     learning_rate=0.05,
#     max_depth=6
# )

# model.fit(X_train, y_train)

# # Predictions
# preds = model.predict(X_test)

# # Evaluation
# rmse = np.sqrt(mean_squared_error(y_test, preds))
# print("Model RMSE:", rmse)

# # Save model
# joblib.dump(model, "model.pkl")

# print("✅ Model trained and saved as model.pkl")

# print("Total Features:", X.shape[1])



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import joblib

# Load dataset
df = pd.read_csv("House Price India.csv")

# Clean column names
df.columns = df.columns.str.strip()

print("Columns:\n", df.columns)

# ✅ Correct feature names
FEATURES = [
    'living area',
    'number of bedrooms',
    'number of bathrooms',
    'grade of the house',
    'Built Year',
    'Postal Code'
]

# Target
y = df['Price']

# Features
X = df[FEATURES]

# Handle missing values
for col in X.columns:
    X[col] = X[col].fillna(X[col].median())

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6
)

model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("Model RMSE:", rmse)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(FEATURES, "features.pkl")

print("✅ Model trained and saved!")