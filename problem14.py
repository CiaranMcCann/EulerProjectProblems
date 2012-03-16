# Problem 14
#
#The following iterative sequence is defined for the set of positive #integers:
#
#n  n/2 (n is even)
#n  3n + 1 (n is odd)
##Using the rule above and starting with 13, we generate the following #sequence:
#
#13  40  20  10  5  16  8  4  2  1
#It can be seen that this sequence (starting at 13 and finishing at 1) #contains 10 terms. Although it has not been proved yet (Collatz Problem#)#, it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
#

from time import time

def algo(n):
	if n % 2 == 0:
		n = n/2
	else:
		n = 3*n + 1
	
	return n

def problem12():

	largestChain = 0
	startingNumber = 0
	for i in range(1,1000000):
		n = i
		chainLenght = 1
		while n != 1:
			n = algo(n)
			chainLenght += 1
	
		if largestChain < chainLenght:
			#print(" New largest = " + str(chainLenght) + " Old largest = " + str(largestChain) + "  answer =  " + str(i))
			largestChain = chainLenght
			startingNumber = i
		
	return startingNumber

	



	

start = time()
print("Start time " + str(start))
print(problem12())
end = time()
print("Time taken " + str(end - start))