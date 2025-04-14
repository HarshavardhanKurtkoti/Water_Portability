import pandas as pd
import numpy as np
import pickle 
import json
import os

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

test_data = pd.read_csv('./data/processed/test_processed.csv')

x_test = test_data.iloc[:,0:-1].values
y_test = test_data.iloc[:,-1].values

model = pickle.load(open('./model/model.pkl', 'rb'))

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

metrics = {
    'accuracy': acc,
    'precision': pre,
    'recall': recall,
    'f1_score': f1
}

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '../model')
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'metrics.json')

with open(output_path, 'w') as f:
    json.dump(metrics, f, indent=4)

