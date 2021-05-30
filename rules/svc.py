import pandas as pd
from sklearn import svm

data = pd.read_csv('data.csv')

x = data['time']
x = x.values
y = data['cpuusage']
y = y.values
label = []

for i in range(len(y)):
    if y[i] < 0.2:
        label.append(0)
    if y[i] > 0.2:
        label.append(1)


for row in data.iterrows():
    print(row[1][1])