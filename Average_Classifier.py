""" 
    Test on the training samples
    by Vincent Jeanselme
    vincent.jeanselme@gmail.com
"""

from DataBase_Extraction.Extraction import *
from Learning.Average import *

# Computes the average images
images_learning = dictionnary_images("DataBase_Extraction/train-labels.idx1-ubyte", 
    "DataBase_Extraction/train-images.idx3-ubyte")
average = average(images_learning, "Images/Average_")

# Computes the training samples and the goals
inputs, targets = input_output("DataBase_Extraction/t10k-labels.idx1-ubyte", 
    "DataBase_Extraction/t10k-images.idx3-ubyte")

def train(training_images, training_labels, learning_average) :
    """ Computes the number of recognized images"""
    recognized = 0
    output = []
    for i in range(len(training_images)) :
        dist = squared_error(training_images[i], learning_average)
        res = forecast(dist)
        output.append(res)
        if res == training_labels[i] :
            recognized += 1

    print("Labels : \n" + str(training_labels))
    print("Forecasts : \n" + str(output))
    print("Total of correct forecasts : " + str(recognized) + " / " + str(len(training_labels)))

train(inputs,targets,average)