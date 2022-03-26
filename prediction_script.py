# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:30:57 2022

@author: blaks
"""

import pandas as pd
import pickle
import json

with open("features_list.json", "r") as f:
    features_list = json.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

X_test_data_raw = pd.read_csv(r'test_set.csv')
X_test_data_raw.drop("Unnamed: 0", axis=1, inplace=True)

X_test_data_raw = scaler.transform(X_test_data_raw)
X_test_data_raw = pd.DataFrame(X_test_data_raw)

X_test_data = X_test_data_raw[features_list]
X_test_data.columns = list(range(X_test_data.shape[1]))

preds = pd.DataFrame(model.predict(X_test_data))
preds.columns = ["Predictions"]
preds.to_csv("test_results.csv", index=False)


