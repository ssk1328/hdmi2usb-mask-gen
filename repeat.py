#!/usr/bin/python

# This defines a repeat like function as used in the hardware fader design doc 
# and genrates required images from them. More documenttion added to each function. 


from PIL import Image
import numpy as np     # numpy

def repeat(count, pixel_list):
	"""  returns a list repeated pixel_list count number of times """		
	mylist = []

	for i in range(count):
		for j in range(len(pixel_list)): 
			mylist.append(pixel_list[j])	

	return mylist

def to_matrix(list_1D,row_length):
	"""  Converts a 1D list to 2D list as per the row_length information """		
	return [list_1D[i:i+row_length] for i in range(0,len(list_1D),row_length)]

def to_image(list_2D, file_name):
	"""  Converts a 2D list with values in [0-255] to image data type and saves as .png file"""		

	list_2D = np.uint8(list_2D)
	im = Image.fromarray(np.asarray(list_2D))
	im.save('%s.png' % file_name)
	return im



def gen_horizoantal_wipe(width, height, time_fraction):
	""" Uses the repeat function to generate a horizoantal wipe and saves the corresponding image as wipe_h.png"""
	W = [255]
	B = [0]
	t = int(time_fraction*width)

	wipe_list = repeat(height, repeat(t , B) + repeat(width-t, W))
	wipe_matrix = to_matrix(wipe_list,width)

	im = to_image(wipe_matrix,'wipe_h')

	return im

def gen_vertical_wipe(width, height, time_fraction):
	""" Uses the repeat function to generate a vertical wipe and saves the corresponding image as wipe_v.png"""
	W = [255]
	B = [0]
	t = int(time_fraction*height)

	wipe_list = repeat(t, repeat(width , B)) + repeat( height - t ,repeat(width, W))

	wipe_matrix = to_matrix(wipe_list,width)
	im = to_image(wipe_matrix,'wipe_v')

	return im

def gen_fuzzy_horizoantal_wipe(width, height, time_fraction):
	""" Uses the repeat function to generate a horizoantal fuzzy wipe and saves the corresponding image as wipe_fuzzy_h.png"""
	W = [255]
	B = [0]

	fuzzy_list = range(1,10+1)

	for i in range(len(fuzzy_list)):
		fuzzy_list[i] = fuzzy_list[i]*25;

	t = int(time_fraction*width)
	wipe_list = repeat(height, repeat(t , B) + fuzzy_list + repeat(width-t-10, W))

	wipe_matrix = to_matrix(wipe_list,width)
	im = to_image(wipe_matrix,'wipe_fuzzy_h')

	return im

def gen_fuzzy_vertical_wipe(width, height, time_fraction):
	""" Uses the repeat function to generate a vertical fuzzy wipe and saves the corresponding image as wipe_fuzzy_h.png"""
	W = [255]
	B = [0]

	fuzzy_list = range(1,10+1)

	for i in range(len(fuzzy_list)):
		fuzzy_list[i] = fuzzy_list[i]*25;

	fuzzy_list_v = []

	for i in range(len(fuzzy_list)):
		for j in range(width):
			fuzzy_list_v.append(fuzzy_list[i])

	t = int(time_fraction*height)
	
	wipe_list = repeat(t, repeat(width , B)) + fuzzy_list_v +repeat( height - t - 10,repeat(width, W))

	wipe_matrix = to_matrix(wipe_list,width)
	im = to_image(wipe_matrix,'wipe_fuzzy_v')

	return im

###
# Main code starts here


gen_horizoantal_wipe(1920,1080, 0.7)
gen_vertical_wipe(1920,1080, 0.7)

gen_fuzzy_horizoantal_wipe(1920,1080, 0.7)
gen_fuzzy_vertical_wipe(1920,1080, 0.7)
