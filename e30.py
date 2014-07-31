
import math
temp=0
result=0
for num in range(2,355000):
	temp=0
	num = str(num)
	for each_char in num:
		temp+=math.pow(int(each_char),5)
	if math.floor(temp) == int(num):
		result+=int(num)	
print (result)
print ('Hello world')