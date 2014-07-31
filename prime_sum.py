import math
num =10

def find(n):
	primes=[]

	for num in range(3,n):
		flag=True
		for x in range(2,math.floor(math.sqrt(num))+1):
			if num%x==0:
				flag=False
				
				break

		if flag:
			
			primes.append(num)
	print(primes)
	return(sum(primes)+2)		

print (find(2000000))