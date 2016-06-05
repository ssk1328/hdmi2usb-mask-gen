#!/usr/bin/python
from PIL import Image  # Pillow
import numpy as np     # numpy

# Function definition is here
def repeat( mylist, number,   pixel):
   "This changes a passed list into this function"
   for i in range(number):
	   mylist.append(pixel);
   return mylist

listH = [];
listV = [];
repeat( listV, 100,  repeat(listH, 300 , 1) );
repeat( listV, 200,  repeat(listH, 400 , 0) );

#listX
#repeat( listX, 100,  repeat(listH, 1280 , 1) );
#repeat( listX, 100,  repeat(listH, 1280 , 0) );


#print "Values outside the function: ", listV

height = len(listV);
width = len(listV[0]);

print "Height: ",height;
print "Width: ", width;

black = (0, 0,255);
white = (255, 255, 255);

listN = [[(128,128,128)]*width]*height;

for i in range(height):
	for j in range(width):
		if listV[i][j] == 1:
			listN[i][j] = white;
		elif listV[i][j] == 0:
			listN[i][j] = black;

# print listN


img = Image.fromarray(np.asarray(listN, dtype=np.uint8))
img.save('test1.png')