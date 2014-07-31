
import math
pro_num=1
pro_den=1
def resolve(num):
	last=num%10
	num=math.floor(num/10)
	first=num%10
	return first,last
count=0
for num in range(10,50):
	for den in range(50,100):
		a,b=resolve(num)
		c,d=resolve(den)
		new_num=0
		new_den=0
		if a==c :
			new_num=b
			new_den=d
		if a==d:
			new_num=b
			new_den=c
		if b==c:
			new_num=a
			new_den=d
		if b==d:
			new_num=a
			new_den=c
		try:	
			if num/den == new_num/new_den and b!=0 :
				pro_num*=new_num
				pro_den*=new_den

				print ('abcd:=')
				print (a,b,' a,b ')
				print (c,d,' c,d ')
				print ('old:-'+str(num)+'/'+str(den)+' New :'+str(new_num)+' /'+str(new_den))
				count+=1
		except:
			pass		
print (count,' count ')

print (pro_num,' / ',pro_den)
"""num=49
den =98
a,b=resolve(num)
c,d=resolve(den)
if a==c :
	new_num=b
	new_den=d
if a==d:
	new_num=b
	new_den=c
if b==c:
	new_num=a
	new_den=d
if b==d:
	new_num=a
	new_den=c
if num/den == new_num/new_den:
	print ('ah')			"""
			