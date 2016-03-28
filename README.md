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
Comparing the new image to the average images created with the learning samples. However we divide the same number by clustering in order to correct some differences (as rotation).
The minimum squared error between the new image and the average images of 0,1 .. 9 will be the best approximation.
#### Library
Needs PIL, struct, sys, math, os, os.path libraries.
#### Python Version
Python 3.4
#### Results
8203 / 10000 of the training data set are correctly classified.