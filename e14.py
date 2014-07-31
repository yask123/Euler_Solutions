cache={}
def find_next(n):
	if n%2==0:
		return(n/2)
	else:
		return(3*n+1)
def calc_length(n):
	temp=n
	length=0
	while(temp>=2):
		
		if temp in cache:
			if n not in cache:
				cache[n]=length+1	
			return(length + cache[temp])
		else:
			temp=find_next(temp)
			length+=1
	
	cache[n]=length+1
	return(length+1)

num=1000000

max_length=0

for num in range(2,num):
		#Finding length of each num
	

	length=calc_length(num)
	if num%10==0:
		print(num," Done!")

	if length>max_length:
		max_length=length
print(max_length)
		




				
