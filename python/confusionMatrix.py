import numpy as np
from icecream import ic
from sklearn.metrics import confusion_matrix

file = "confusion.csv"
rawData = np.genfromtxt(file,delimiter=",")
trueValue = rawData[:,0]
predictedValue = rawData[:,1]

# compute confusion matrix
confusionMatrix = confusion_matrix(trueValue, predictedValue)
ic(confusionMatrix)