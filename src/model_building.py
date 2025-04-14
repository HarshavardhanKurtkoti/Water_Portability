import pandas as pd
import numpy as np
import pickle
import os

from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv('data/processed/test_processed.csv')

X_train = train_data.drop(columns=['Potability'],axis=1)
y_train = train_data['Potability']

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, '../model')

os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, 'model.pkl')
pickle.dump(clf, open(model_path, 'wb'))