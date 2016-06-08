from PIL import Image
im = Image.open('a2.jpg')

pix = list(im.getdata())
#pixel = im.load()
width, height = im.size

pixn = [0]*(width*height)

for i in range(len(pix)):

	if pix[i] > 128 :
		pixn[i] = 1
	else:
		pixn[i] = 0

length = len(pixn)

print "New length is %d" % length
print "New width  is %d" % width
print "New height is %d" % height

print pixn

im2 = Image.new( 'L', im.size, "black") # create a new black image
pixels = im2.load() # create the pixel map

for i in range(im2.size[0]):    # for every pixel:
	for j in range(im2.size[1]):
		loc = j*im2.size[0] + i
		if pixn[loc] == 1 :
			pixels[i,j] = 0 #(255, 255, 255) # set the colour accordingly
		else:
			pixels[i,j] = 255 #(0, 0, 0) # set the colour accordingly


im2.save('a3.jpg')
