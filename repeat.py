#!/usr/bin/python
from PIL import Image
import numpy as np     # numpy


def repeat(count, pixel_list):
	"""  repeat function """		
	mylist = []

	for i in range(count):
		for j in range(len(pixel_list)): 
			mylist.append(pixel_list[j])	

	return mylist

def to_matrix(list_1D,row_length):
	return [list_1D[i:i+row_length] for i in range(0,len(list_1D),row_length)]

def to_image(list_2D):

	list_2D = np.uint8(list_2D)
	im = Image.fromarray(np.asarray(list_2D))
	im.save('wipe.png')
	return im


W = [255]
B = [0]
width = 500
height = 300
t = int(width*0.4)

e = repeat(height, repeat(t , B) + repeat(width-t, W))

f = to_matrix(e,width)

to_image(f)
