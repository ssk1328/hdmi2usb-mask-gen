#!/usr/bin/python

from PIL import Image

#Function definition here
def conv2grayscale(filename):

	col = Image.open(filename)
	gray = col.convert('L')
	bw = gray.point(lambda x: 0 if x<128 else 255, '1')
	return bw


def image2list(im):
	
	pix = list(im.getdata())
	width, height = im.size
	pixn = [-1]*(width*height)

	for i in range(len(pix)):

		if pix[i] > 128 :
			pixn[i] = 1
		else:
			pixn[i] = 0

	length = len(pixn)

	print ("New length is %d" % length)
	print ("New width  is %d" % width)
	print ("New height is %d" % height)

	return pixn



bw = conv2grayscale("a1.jpg")
#bw.save("a2.jpg")
pixn = image2list(bw)
