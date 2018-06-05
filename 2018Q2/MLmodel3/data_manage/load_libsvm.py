from sklearn.datasets import load_svmlight_file
import time

print(time.time())
filename = "apk_libsvm.dat"
data = load_svmlight_file(filename)
X, y = data[0], data[1]
X = X.todense()
print(time.time())

import pandas as pd
import numpy as np

df = pd.read_csv("transfered.csv")

y_data = np.array(df['is_malware'])
del df['is_malware']

X_data = np.array(df)
print(time.time())
