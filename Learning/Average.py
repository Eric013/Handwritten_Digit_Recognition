""" 
	Library for analysing distance between images
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from PIL import Image

def average(images, save_path = None) :
	""" Computes the average image for a dictionnary of images :
		for each key, it computes the average image and save it 
		at save_path if save_path is not None """
	average = []

	for number in images.keys() :
		res = [sum([images[number][image][pixel] 
			for image in range(len(images[number]))])/len(images[number]) 
			for pixel in range(len(images[number][0]))]
		if save_path != None :
			imNew = Image.new("L" ,(28,28))  
			imNew.putdata(res)
			imNew.save(save_path + str(number), "JPEG")
		average.append(res)

	return average

def squared_error(image, numbers_image) :
	""" Computes a vector of squared error between an image 
		and a list of others images of same dimension
		The result has the same length than numbers_image """
	res = []

	for number in range(len(numbers_image)) :
		res.append(sum([(image[pixel] - numbers_image[number][pixel])**2 
			for pixel in range(len(image))]))
	
	return res

def forecast(distance_vector) :
	""" Returns the index of the lowest squared error """
	return distance_vector.index(min(distance_vector))
