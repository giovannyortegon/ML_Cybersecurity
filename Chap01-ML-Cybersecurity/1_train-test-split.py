#!/usr/bin/env python3
from sklearn.model_selection import train_test_split
import pandas as pd

# Read csv File
df = pd.read_csv("north_korea_missile_test_database.csv")
y = df["Missile Name"]      # Save in Y Missile Name Column
X = df.drop("Missile Name", axis=1)  # Remove Missile Name Column

# Random Split data 80% train / 20% test
X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size = 0.2, random_state=31
        )

# Vaidation set split
X_train,  X_val, y_train, y_val = train_test_split(
            X_train, y_train, test_size=0.25, random_state=31
        )

print("X train")
print(len(X_train))
print("y train")
print(len(y_train))
print("X valid")
print(len(X_val))
print("y valid")
print(len(y_val))
print("X test")
print(len(X_test))
print("y test")
print(len(y_test))
