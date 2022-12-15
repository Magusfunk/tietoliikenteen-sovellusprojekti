import numpy as np
from icecream import ic
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

file = "confusion.csv"
rawData = np.genfromtxt(file,delimiter=",")
trueValue = rawData[:,0]
predictedValue = rawData[:,1]
confusionMatrix = confusion_matrix(trueValue, predictedValue)

fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.matshow(confusionMatrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confusionMatrix.shape[0]):
    for j in range(confusionMatrix.shape[1]):
        ax.text(x=j, y=i,s=confusionMatrix[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()
