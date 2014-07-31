with open('adj.txt') as f:
	data = f.read()

data=data.strip()
num=''
i=0
prod=1
maxx=0
temp=[]
max_nums=[]
for each in data:
	if each=='\n':
		pass
	else :
		num = num+str(each)
r=int(num)%4
print(r)		
while(i<len(num)-r):


 	number=num[i:i+13]
 	for each in number:
 	 	prod*=int(each)
 	 	temp.append(each)

 	if maxx<prod:
 		maxx=prod
 		max_nums=temp 
 	i+=1
 	prod=1
 	temp=[]	

print(maxx)
print(max_nums)			
