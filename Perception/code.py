from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np

AB = np.array([[10, 1],
               [5, 2],
               [7, 1],
               [4, 2.5],
               [4, 1],
               [5, 0.5],
               [8, 0.5],
               [8, 1],
               [7, 0.3],
               [6, 0.3]])
C = np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0])

lr = Perceptron()
lr.fit(AB, C)

# pred = lr.predict(AB)
# print(pred)
# print(accuracy_score(C, pred))

X_test = [[4, 3]]
Y_pred = lr.predict(X_test)
print(Y_pred[0])
