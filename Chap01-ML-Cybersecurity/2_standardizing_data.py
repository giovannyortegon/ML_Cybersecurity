#!/usr/bin/env python3
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("file_pe_headers.csv", sep=",")
X = data.drop(["Name", "Malware"], axis=1).to_numpy()

# print(X)
X_standardized = StandardScaler().fit_transform(X)

print(X_standardized)
