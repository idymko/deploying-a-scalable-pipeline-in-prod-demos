import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import yaml
import joblib

print("\n--- Running train.py ---\n")

# Load parameters
with open('params.yaml') as f:
    params = yaml.safe_load(f)
C = params['train']['C']

print("Parameter train.C", C)

# Load data
X = pd.read_csv("X.csv")
y = pd.read_csv("y.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=23)

# Train model
lr = LogisticRegression(C=C)
lr.fit(X_train, y_train)

# Save the model
joblib.dump(lr, 'output/model.pkl')

# Predictions and evaluation
preds = lr.predict(X_test)
f1 = f1_score(y_test, preds)
print(f"F1 score: {f1:.4f}")

# Save the score to a file for traceability
with open('output/score.txt', 'w') as score_file:
    score_file.write(f"F1 score: {f1:.4f}\n")