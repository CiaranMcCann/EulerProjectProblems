# Problem 12
#
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
#1: 1
#3: 1,3
#6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
#
#
# NOTE - running time quite slow, nearly a minute to get the answer
# maybe use a seive method to get the factors instead. Works anyway.

from time import time
import math


def factors(n):
	fact=[1,n]
	check=2
	rootn= math.sqrt(n)
	factorCount = 0
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n/check)
		check+=1
	if rootn==check:
		fact.append(check)
	return  fact



def triangleNum():
	for i in range(1, 90000000):
		k = math.sqrt(8*i + 1)
		if k == int(k):
			if len(factors(i)) >= 500:
				return " tNUm = " + str(i) 
	
start = time()
print("Start time " + str(start))
print( triangleNum() ) #triangleNum(1))
end = time()
print("Time taken " + str(end - start))