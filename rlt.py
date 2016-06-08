l1 = [1,1,1,1,1,0,0,1,0,0];

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

print l2
summ = 0

for i in range(len(l2)):
	summ = summ + l2[i][0];

l3 = [-1]*summ;
ptr = 0;

print summ

for i in range(summ):

	print l2

	if l2[ptr][0] > 0 :
		l3[i] = l2[ptr][1];
		l2[ptr][0] = l2[ptr][0] -1 ;
	else:
		ptr = ptr+1;
		l3[i] = l2[ptr][1];
		l2[ptr][0] = l2[ptr][0] -1 ;
print "\n"
print l1
print l3




