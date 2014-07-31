import math
def term(n):
	sum=0
	sum = (n*(n+1))/2
	return(sum)
def count_factors(n):
	count=0
	for num in range(1,math.floor(math.sqrt(n))):
		if n%num==0:
			count = count+1

	return(2*count)

def find_result():
	i=1
	while(True):
		
		if count_factors(term(i))>500:
			break
		
		i=i+1
	return(i)	
print(find_result())