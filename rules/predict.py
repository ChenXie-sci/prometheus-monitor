import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,plot_confusion_matrix


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

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1, random_state = 1)

model = LinearRegression()

model.fit(x_train.reshape(-1,1), y_train)

pred = model.predict(x_test.reshape(-1,1))


label2 = []
for i in range(len(y_test)):
    if y_test[i] < 0.2:
        label2.append(0)
    if y_test[i] > 0.2:
        label2.append(1)

label1 = []
for i in range(len(pred)):
    if pred[i] < 0.2:
        label1.append(0)
    if pred[i] > 0.2:
        label1.append(1)
sum = 0
for i in range(len(label1)):
    if label1[i] == label2[i]:
        sum += 1

accuracy = sum / len(label1)

print(accuracy)
