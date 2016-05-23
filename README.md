# Handwritten_Digit_Recognition
Analysis of the MNIST database : http://yann.lecun.com/exdb/mnist/

## Project organization
The root directory contains the different tests on the training dataset.
Execute this file for observing the following results.
### Data_Base_Extraction
Contains the database and the library for extracting data.
### Learning
Contains the different ways for learning and predict the digit.
### Images
Contains the different average images.

## Methods used
### Average comparison
#### Idea
Comparing the new image to the average images created with the learning samples.
The minimum squared error between the new image and the average image of 0,1 .. 9 will be the best approximation.
#### Library
Needs PIL, struct, sys, math, os, os.path libraries.
#### Python Version
Python 3.4
#### Results
8203 / 10000 of the training data set are correctly classified.

### Clustering and average comparison
#### Idea
Comparing the new image to the average images created with the learning samples. However we divide the images of a same number by clustering in order to correct some differences (as rotation) and reduce the dimension roblem.
For the clustering, we use the KMeans algorithm.
The minimum squared error between the new image and the average images of 0,1 .. 9 will be the best approximation.
#### Library
Needs PIL, struct, sys, math, os, os.path libraries.
#### Python Version
Python 3.4
#### Results
* 9024 / 10000 of the training data set are correctly classified with 5 classes and 20 iterations.
* 9241 / 10000 of the training data set are correctly classified with 10 classes and 20 iterations.

### Clustering and K nearest neighbors
#### Idea
Comparing the new image to the K classes obtained by the algorithm of KMeans.
However the best approximation is obtained by the K nearest neighbors : we observe the closest images and when we have more than K identic label, we stop the algorithm and return this label as the best forecast.
#### Library
Needs PIL, struct, sys, math, os, os.path libraries.
#### Python Version
Python 3.4
#### Results
* 9024 / 10000 of the training data set are correctly classified with 10 classes, 20 iterations and 1 neighbors. (coherent with the precious way of computing the best approximation)
* 8763 / 10000 of the training data set are correctly classified with 10 classes, 20 iterations and 2 neighbors.
* 8462 / 10000 of the training data set are correctly classified with 10 classes, 20 iterations and 3 neighbors.
* 8030 / 10000 of the training data set are correctly classified with 10 classes, 20 iterations and 4 neighbors.
* 7535 / 10000 of the training data set are correctly classified with 10 classes, 20 iterations and 5 neighbors.

* 9562 / 10000 of the training data set are correctly classified with 100 classes, 20 iterations and 1 neighbors.
* 9535 / 10000 of the training data set are correctly classified with 100 classes, 20 iterations and 2 neighbors.
* 9457 / 10000 of the training data set are correctly classified with 100 classes, 20 iterations and 3 neighbors.
* 9401 / 10000 of the training data set are correctly classified with 100 classes, 20 iterations and 4 neighbors.
* 9356 / 10000 of the training data set are correctly classified with 100 classes, 20 iterations and 5 neighbors.

### Future work
* Try the KNN algorithm on the full dataset with a KDTree structure
