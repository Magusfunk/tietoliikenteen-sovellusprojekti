import pandas as pd
import numpy as np
from icecream import ic
from tensorflow import keras
from tensorflow.keras import layers

num_classes = 6

file = "python\export.csv"
rawData = np.genfromtxt(file,delimiter=",")
coordinates = rawData[:,5:8]
label = rawData[:,9].reshape((len(rawData),1))
label = keras.utils.to_categorical(label,num_classes)

#<------------------------->

from sklearn.model_selection import train_test_split
input_shape = 3
coordinates_train,coordinates_test,label_train,label_test = train_test_split(coordinates,label,test_size=0.2)

#<------------------------->

model = keras.Sequential(
    [
    keras.Input(shape=input_shape),
    layers.Dense(num_classes,activation="relu",name="hiddenLayer"),
    layers.Dense(num_classes,activation="softmax",name="OutputLayer"),
    ]
)

#<------------------------->

batch = 10
epochs = 100
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(coordinates_train,label_train,batch_size=batch,epochs=epochs)

score = model.evaluate(coordinates_test, label_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

#<------------------------->

coordinates_predict = model.predict(coordinates_train)
#for row in range(len(coordinates_predict)):
#  print(np.argmax(coordinates_predict[row,:]),np.argmax(label_train[row]))

weights = model.get_weights()
# for row in weights:
#     ic(row)
    
        
biases = [var for var in model.variables if "bias" in var.name]
# weights = [var for var in model.variables if "weight" in var.name]
ic(biases,weights)

with open('./weights.txt', mode='w') as f:
    f.write(str(weights))
    f.close
    
with open('./biases.txt', mode='w') as f:
    f.write(str(biases))
    f.close
    