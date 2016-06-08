from PIL import Image

col = Image.open("f1.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("f2.jpg")

im = Image.open('f2.jpg')
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


#print pixn;



#l1 = [1,1,1,1,1,1,0,0,0,0];
l1 = pixn;

l2 = [ [-1] * 2 ] * (len(l1)+1);

ptr = 0;

for i in range(len(l1)):
	if l1[i] == l2[ptr][1]:
		l2[ptr][0] = l2[ptr][0] + 1;

	else:
		ptr = ptr+1
		l2[ptr] = [1 , l1[i]];

val = [-1, -1];
while val in l2:
	l2.remove(val)

#print l1
#print l2;
summ = 0

for i in range(len(l2)):
	summ = summ + l2[i][0];

l3 = [-1]*summ;
ptr = 0;

print summ

for i in range(summ):

#	print l2

	if l2[ptr][0] > 0 :
		l3[i] = l2[ptr][1];
		l2[ptr][0] = l2[ptr][0] -1 ;
	else:
		ptr = ptr+1;
		l3[i] = l2[ptr][1];
		l2[ptr][0] = l2[ptr][0] -1 ;

#print l3;

pixk = l3;

im2 = Image.new( 'L', im.size, "black") # create a new black image
pixels = im2.load() # create the pixel map

for i in range(im2.size[0]):    # for every pixel:
	for j in range(im2.size[1]):
		loc = j*im2.size[0] + i
		if pixk[loc] == 1 :
			pixels[i,j] = 0 #(255, 255, 255) # set the colour accordingly
		else:
			pixels[i,j] = 255 #(0, 0, 0) # set the colour accordingly


im2.save('f3.jpg')




