"""Solution to euler's 13 problem"""

import collections
import e3
a=e3.findfactors(100)
print(a)
counter=collections.Counter(a)#Return a dictionary of frequency of elements in the prime list
pro=1

for each_key in counter:
	pro*=(counter[each_key]+1)#Calculate (a+1)*(b+1)*...etc
