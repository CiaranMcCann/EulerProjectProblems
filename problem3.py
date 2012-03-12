# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# @date 11/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
#
# TODO - optimizes

from time import time
import math

def LargestPrimeBetween(r1, r2):
	for i in reversed(range(r1+1, int(math.sqrt(r2)*10))):		
		numUpToi = 1 #TODO need to test for 2	
		while numUpToi < i-1:
			numUpToi += 2 # To skip even numbers
			if i % numUpToi == 0:				
				break
			
			if numUpToi == i-2:
				return i


def largestPrimeFactor(n):
	largestPrimeFactor = n;
	while (True):
		prime = LargestPrimeBetween(0, (largestPrimeFactor))
		if n % prime == 0:
			return prime
		else:
			largestPrimeFactor = prime


start = time()
print(start)
print(largestPrimeFactor(13195))	
end = time()
print(end - start)
