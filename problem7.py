
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
#
# @date 12/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
#
# @timeTaken 1.7669999599456787

import math
from time import time

def chunk(collection, chuckSize):
    return [collection[i:i+chuckSize] for i in range(0, len(collection), chuckSize)]

def printGridArray(array,width = 10):
	rows = chunk(array,width)
	print(" ")
	for row in rows:
		print(row)
	print(" ")


def remove_all(element, list):
    return filter(lambda x: x != element, list)

def genPrimeList(upTo):
	primeNth = 0
	numbers = []
	for i in range(0,upTo):
		numbers.append(i)
	numbers[1] = 0

	p = 2
	n = 2
	#printGridArray(numbers)
	while True:
		n = 2
		while n*p < len(numbers): # remove all multplies
			numbers[n*p] = 0
			n += 1
		
		while p < len(numbers): # find next multiple to remove
			p += 1

			if p == len(numbers):
				return numbers

			if numbers[p] != 0:
				p = numbers[p]
				primeNth += 1
				break
			
			
def findNthPrime(n,range):
	ans = list(remove_all(0, genPrimeList(range) ))[n-1]
	print (" The " + str(n) + " th prime is " + str(ans))

start = time()
print(start)

findNthPrime(10001,1310000)

end = time()
print(end - start)



