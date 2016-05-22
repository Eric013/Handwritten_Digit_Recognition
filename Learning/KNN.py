""" 
	Library for finding the nearest class following
	the K nearest neighbor algorithm
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

def squared_error(image, numbers_image) :
	""" Computes a dictionary of squared error between an image 
		and a list of others images of same dimension
		The result has the same length than numbers_image """
	res = {}

	for number in numbers_image.keys() :
		res[number] = []
		for img in range(len(numbers_image[number])) :
			res[number].append(sum([(image[pixel] - numbers_image[number][img][pixel])**2 
				for pixel in range(len(image))]))
	
	return res

def k_nearest_neighbor(distance_dictionary, K = 5) :
	""" Returns the index of the class which has the K nearest neighbors. 
	(K < min(len([distance_dictionary[i] 
		for i in distance_dictionary.keys()]))) """
	value = []
	for number in distance_dictionary.keys() :
		for dist in distance_dictionary[number] :
			value.append((number, dist))
	value.sort(key=lambda x: x[1])

	tot = [0] * len(distance_dictionary.keys())

	for j in value :
		if max(tot) < K :
			tot[j[0]] += 1
		else :
			break
				
	return tot.index(max(tot))