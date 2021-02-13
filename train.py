import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import json

X = pd.read_csv("data_processed.csv")
y = pd.read_csv("labels.csv")
print(X.shape, ': X')
print('y: ', y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2)

clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred, normalize=True)
print(acc)

with open("metrics.json", 'w') as outfile:
    json.dump({
        "accuracy": acc
    }, outfile)
