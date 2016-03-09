""" 
    Library for extracting data from the data set
    by Vincent Jeanselme
    vincent.jeanselme@gmail.com
"""

import struct, sys, math, os, os.path
from PIL import Image

def dictionnary_images(index_fname, images_fname) :
    """ Creates a dictionary where the keys are the label linked
        to the images which are the items """
    images_f = open(images_fname,"rb")
    images_header_fmt = ">4L"
    images_header = struct.unpack(images_header_fmt, images_f.read(struct.calcsize(images_header_fmt)))

    index_f = open(index_fname,"rb")
    index_header_fmt = ">2L"
    index_header = struct.unpack( index_header_fmt, index_f.read(struct.calcsize( index_header_fmt)))

    magic, nimages, height, width = images_header
    magic, nlabels = index_header
     
    classify = {}

    for n in range(100):
        label = int.from_bytes(index_f.read(1),byteorder='big')
        img = []
        for i in range(height * width) :
            img.append(int.from_bytes(images_f.read(1),byteorder='big'))

        try :
            classify[label].append(img)
        except KeyError:
            classify[label] = []
            classify[label].append(img)

    return classify

def input_output(index_fname, images_fname) :
    """ Creates two lists : one for the image : input and one 
        for the label associated : output """
    images = dictionnary_images(index_fname, images_fname)
    inputs = []
    for key in images.keys() :
        for l in images[key] :
            inputs.append(l)

    targets = []
    for key in images.keys() :
        for l in range(len(images[key])) :
            targets.append(key)

    return inputs, targets