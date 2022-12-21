import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import confusion_matrix

def headerFileGenerator(inputData):
    inputs = 3
    outputs = 6
    weights = np.array2string(inputData[0].flatten(),separator=",")
    biases = np.array2string(inputData[1].flatten(),separator=",")
    fileData = ["#define WEIGHTSBIASES_H\n",
            f"float weights[{inputs}][{outputs}] = ",
            "{",weights[1:-1],"};\n\n",
            f"float biases[{outputs}] = ",
            "{",biases[1:-1],"};\n\n"]
    with open('weightsBiases.h', 'w') as file:
            file.writelines(fileData)
    file.close  
    
#<------------------------->
#Luetaan data csv:stä  
num_classes = 6
file = "python\export.csv"
rawData = np.genfromtxt(file,delimiter=",")
coordinates = rawData[:,5:8] / 100
ic(coordinates)
label = rawData[:,9].reshape((len(rawData),1))
label = keras.utils.to_categorical(label,num_classes)

#<------------------------->
#Jaetaan data testidataan ja treenidataan
from sklearn.model_selection import train_test_split
input_shape = (3)
coordinates_train,coordinates_test,label_train,label_test = train_test_split(coordinates,label,test_size=0.2, random_state=42, shuffle=True)

#<------------------------->
#Mallin määrittely
model = keras.Sequential(
    [
    keras.Input(shape=input_shape),    
    layers.Dense(num_classes,activation="softmax",name="OutputLayer",)
    ]
)

#<------------------------->
#Mallin toteutus ja tarkkuus
batch = 38
epochs = 300
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(coordinates_train,label_train,batch_size=batch,epochs=epochs)
score = model.evaluate(coordinates_test, label_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

#<------------------------->
#Mallin testaus ja painoarvojen kirjaus tiedostoon
coordinates_predict = model.predict(coordinates_train)
count = 0
for i in range(len(coordinates_predict)):
    print("Predict:", np.argmax(coordinates_predict[i]),np.argmax(label_train[i]))
    if np.argmax(coordinates_predict[i]) == np.argmax(label_train[i]):
        count += 1
print("Tarkkuus prosentteinta: ", (count / len(coordinates_predict)) * 100,"%")

weights = model.get_weights()
headerFileGenerator(weights)