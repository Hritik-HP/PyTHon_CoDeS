from matplotlib import pyplot as plt
import numpy as np
s = np.array([[50, 60, 70, 90], [20, 70, 40, 70],
             [30, 10, 30, 80], [23, 32, 43, 23]])
X = ["Q1", "Q2", "Q3", "Q4"]
Y1 = s[:, 0]
plt.plot(X, Y1, 'p-r', mfc='b', mec='r', ms=10, label="delhi")
plt.legend()
Y2 = s[:, 1]
plt.plot(X, Y2, '*--b', mfc='k', mec='c', ms=10, label="mumbai")
plt.legend()
Y3 = s[:, 2]
plt.plot(X, Y3, 'o:c', mfc='r', mec='b', ms=10, label="rajasthan")
plt.legend()
Y4 = s[:, 3]
plt.plot(X, Y4, 's-r', mfc='c', mec='c', ms=10, label="gujrat")
plt.legend()
plt.suptitle("Sales of Iphone13")
plt.show()
