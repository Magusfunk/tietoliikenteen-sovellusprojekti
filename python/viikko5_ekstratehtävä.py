import numpy as np
from icecream import ic
from tensorflow import keras
from tensorflow.keras import layers


def headerFileGenerator(input):
    inputs = 3
    outputs = 6
    weights = np.array2string(input[0].flatten(),separator=",")
    biases = np.array2string(input[1].flatten(),separator=",")
    
    data = [f"int weights[{inputs}][{outputs}] = ",
            "{",weights[1:-1],"};\n\n",
            f"int biases[{outputs}] = ",
            "{",biases[1:-1],"};\n\n"]

    with open('weightsBiases.h', 'w') as file:
            file.writelines(data)
    file.close  
    
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
    # layers.Dense(num_classes,activation="relu",name="hiddenLayer"),
    layers.Dense(num_classes,activation="softmax",name="OutputLayer"),
    ]
)

#<------------------------->

batch = 38
epochs = 300
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(coordinates_train,label_train,batch_size=batch,epochs=epochs)

score = model.evaluate(coordinates_test, label_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

#<------------------------->

coordinates_predict = model.predict(coordinates_train)

weights = model.get_weights()
ic(weights[0])   
ic(weights[1])  
     
with open('test.npy', 'wb') as f:
    np.save(f, weights[0])
    np.save(f, weights[1])

headerFileGenerator(weights)