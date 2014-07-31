from timeit import default_timer as timer
start = timer()
def find_sum(limit):
	limit*=limit
	num=1
	add=2
	result=1
	while num<limit:
		for i in range(4):
			num+=add
			result+=num
		add+=2
	return result
print (find_sum(1001))
elapsed_time = (timer() - start) * 1000 # s --> ms
print ("Found in %r ms." % (elapsed_time))		
			