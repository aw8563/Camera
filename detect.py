import tensorflow
import numpy

from PIL import Image
from matplotlib import pyplot

class Detect():
    
    def __init__(self, model = None):
        self.model = model
        self.image = None
        self.imageArray = None


    def showImage(self, image = None):
        if not image:
            image = self.image

        print(self.imageArray)
        pyplot.imshow(image)
        pyplot.show()
    
    def setImage(self, image):
        self.image = image
        self.imageArray = numpy.array(image)


    def evaluate(self, image = None):
        pass


def main():
    detect = Detect()
    detect.setImage(Image.open('test.jpg'))
    
    detect.showImage()

if __name__ == '__main__':
    pass
    # main()


# mnist = tensorflow.keras.datasets.mnist

# trainingData, testData = mnist.load_data()

# trainingInput, trainingOutput = trainingData
# testInput, testOutput = testData

# trainingInput = tensorflow.keras.utils.normalize(trainingInput)
# testInput = tensorflow.keras.utils.normalize(testInput)



# model = tensorflow.keras.models.Sequential()
# model.add(tensorflow.keras.layers.Flatten())

# model.add(tensorflow.keras.layers.Dense(128, activation = tensorflow.nn.relu))
# model.add(tensorflow.keras.layers.Dense(128, activation = tensorflow.nn.relu))
# model.add(tensorflow.keras.layers.Dense(10, activation = tensorflow.nn.softmax))


# print("START TRAINING\n\n")
# model.compile(optimizer= 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
# model.fit(trainingInput, trainingOutput, epochs = 3)

# model.save('firstModel.model')

# model = tensorflow.keras.models.load_model('firstModel.model')

# result = model.predict(testInput)
