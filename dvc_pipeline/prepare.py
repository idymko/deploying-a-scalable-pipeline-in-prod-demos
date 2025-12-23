import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import yaml

print("\n--- Running prepare.py ---\n")

# Load parameters
with open('params.yaml') as f:
    params = yaml.safe_load(f)
data_path = params['prepare']['data_path']
df = pd.read_csv(data_path)

X = df["feature"].values
y = df["label"].values

scaler = MinMaxScaler()
X = scaler.fit_transform(X.reshape(-1, 1))
print(X)

np.savetxt("X.csv", X)
np.savetxt("y.csv", y)
