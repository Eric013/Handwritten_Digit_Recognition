""" 
	Library for analysing distance between images and classify it by clustering
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from PIL import Image
from .Average import *

def cluster(image_list, number_of_class, iteration) :
	""" Computes a clustering between the different images of the
		list using the Kmeans algorithm in number_of_class classes"""
	classes_average = [image_list[i] for i in range(number_of_class)]
	for ite in range(iteration) :
		classes = [[] for i in range(number_of_class)]
		for image in image_list :
			# Add the image to the closest class
			dist = squared_error(image, classes_average)
			k = forecast(dist)
			classes[k].append(image)
		# Compute the new average of the classes
		classes_average = [[sum([classes[k][image][pixel] 
			for image in range(len(classes[k]))])/len(classes[k]) 
			for pixel in range(len(classes[k][0]))]
			for k in range(number_of_class)]
	
	return classes_average

def average_clustering(images, number_of_class = 5, iteration = 100, save_path = None) :
	""" Computes the average image for a dictionnary of images :
		for each key, it computes the average image and save it 
		at save_path if save_path is not None """
	average = {}
	for number in images.keys() :
		average[number] = cluster(images[number], number_of_class, iteration)
		for sub_section in range(len(average[number])) :
			if save_path != None :
				imNew = Image.new("L" ,(28,28))  
				imNew.putdata(average[number][sub_section])
				imNew.save(save_path + str(number) + "_" + str(sub_section), "JPEG")

	return average

def squared_min_error(image, numbers_image) :
	""" Computes a vector of squared error between an image 
		and a list of others images of same dimension
		The result has the same length than numbers_image """
	res = []
	for number in range(len(numbers_image)) :
		inter = squared_error(image, numbers_image[number])
		res.append(min(inter))
	return res