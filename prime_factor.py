"""This module contains the function  find_prime_factors() which takes a number as an argument and returns a list of all the prime factors.
This is one of the most fastest module available.The algorithm is based on the simple PRIME FACTORIZATION technique 
Written by Yask Srivastava @yask123 """

import math
def is_prime(num):
	for n in range(2,math.floor(math.sqrt(num)+1)):
		if num%n==0:
			return False
	return True			

def find_prime_factors(num):
	primes=[]
	for n in range(2,math.floor(num/2)+2):#The maximum value of the factor could only be half of the number
		if is_prime(num):
			primes.append(math.floor(num))
			break
		if is_prime(n) and num %n==0:
			num=num/n
			primes.append(n)
			while num%n ==0:
				num=num/n
				primes.append(n)
			
	return(primes)		


