# Problem 10
#
#Find the greatest product of five consecutive digits in the 1000-digit number.
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# @date 12/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/

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

primes = genPrimeList(2000000)
print(sum(primes))