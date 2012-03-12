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
		#print( " FOUND prime " + str(prime))
		if n % prime == 0:
			return prime
		else:
			largestPrimeFactor = prime


start = time()
print(start)
print(largestPrimeFactor(60085147514))	
end = time()
print(end - start)
#print(largestPrimeFactor(600851475143))
