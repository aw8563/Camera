import tensorflow
import numpy as np
import cv2
import random
import os

from matplotlib import pyplot as plot
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D, MaxPooling2D

RESOLUTION = (160,80)
trainingData = []

def getImageArray(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, RESOLUTION)
    image = np.array(image, dtype='float32')
    
    return image

def getNumpyArray():
    for f in os.listdir("empty/"):
        try:
            trainingData.append([getImageArray('empty/' + f), 0])
        except Exception as e:
            print(e)

    for f in os.listdir("person/"):
        try:
            trainingData.append([getImageArray('person/' + f), 1])
        except Exception as e:
            print(e)

    random.shuffle(trainingData)

def showImage(img):
    plot.imshow(img)
    plot.show()

# getNumpyArray()
def buildTrainingInputs():
    # trainingInput = [data[0] for data in trainingData]
    # trainingOutput = [data[1] for data in trainingData]

    # trainingInput = np.array(trainingInput)
    # trainingOutput = np.array(trainingOutput)

    # np.save("trainingInput", trainingInput)
    # np.save("trainingOutput", trainingOutput)


    # trainingInput = np.load("trainingInput.npy")
    # trainingOutput = np.load("trainingOutput.npy")

    # trainingInput = trainingInput.reshape(238,80,160,1)
    return trainingInput, trainingOutput

def buildModel():
    model = Sequential()

    model.add(Conv2D(64, (3,3), input_shape = (80, 160, 1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))

    model.add(Conv2D(64, (3,3), input_shape = (80, 160, 1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))


    model.add(Flatten())
    model.add(Dense(64))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    return model

def trainModel(model, trainingInput, trainingOutput):

    print("START TRAINING\n\n")
    model.compile(optimizer= 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    model.fit(trainingInput, trainingOutput,batch_size = 32, validation_split = 0.1, epochs = 5)

    model.save("bestModel.model")



def predictImage(model, imgPath):
    try:
        img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, RESOLUTION)
        img = img.reshape(80,160,1)
        img = np.array([img])
        print(model.predict(img))
    except Exception as e:
        print(e)



model = tensorflow.keras.models.load_model('bestModel.model')
