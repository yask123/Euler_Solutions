import math
a,b=1,1
term=2

while 1:
	if math.floor(len(str(b)))>=1000:
		break
	a,b=b,a+b
	term+=1
print (term)		