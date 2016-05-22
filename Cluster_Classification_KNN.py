""" 
    Test on the training samples
    by Vincent Jeanselme
    vincent.jeanselme@gmail.com
"""

from DataBase_Extraction.Extraction import *
from Learning.Clustering import *
from Learning.KNN import *

# Computes the average images
images_learning = dictionnary_images("DataBase_Extraction/train-labels.idx1-ubyte", 
    "DataBase_Extraction/train-images.idx3-ubyte")
average = average_clustering(images_learning, 100, 20, "Images/Average_Clustering_")

# Computes the training samples and the goals
inputs, targets = input_output("DataBase_Extraction/t10k-labels.idx1-ubyte", 
    "DataBase_Extraction/t10k-images.idx3-ubyte")

def train(training_images, training_labels, learning_average, number_of_neighbor) :
    """ Computes the number of recognized images"""
    recognized = 0
    output = []
    for i in range(len(training_images)) :
        dist = squared_error(training_images[i], learning_average)
        res = k_nearest_neighbor(dist, number_of_neighbor)
        output.append(res)
        if res == training_labels[i] :
            recognized += 1

    print("Labels : \n" + str(training_labels))
    print("Forecasts : \n" + str(output))
    print("Total of correct forecasts : " + str(recognized) + " / " + str(len(training_labels)))

train(inputs,targets,average, 1)
train(inputs,targets,average, 2)
train(inputs,targets,average, 3)
train(inputs,targets,average, 4)
train(inputs,targets,average, 5)
train(inputs,targets,average, 6)
train(inputs,targets,average, 7)
train(inputs,targets,average, 8)
train(inputs,targets,average, 9)
train(inputs,targets,average, 10)