import math
data ={}

def isPrime(n):
	global data
	if n in data:
		return data[n]

	for num in range(2,math.floor(math.sqrt(n)+1)):
		if n%num == 0:
			data[n]=False
			return False
	data[n]=True
	return True
count =0
data ={}

for num in range (2,1000000):
	q=False
	num=str(num)
	for i in range(len(num)):
		if (isPrime(int(num[i:]+num[:i]))):
			q=True
		else:
			q=False
			break
	if q:		
		count+=1			
print (count)			
