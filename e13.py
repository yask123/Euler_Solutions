with open('e13.txt') as f:
	data = f.read()
cluster=[]
number=''
data = data +'\n'
for each_element in data:
	
	if each_element=='\n':
		cluster.append(int(number))
		number=''
		
		
		pass
	else:
		number+=each_element		

print(str(sum(cluster))[:10])


