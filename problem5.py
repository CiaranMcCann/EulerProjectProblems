# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# @date 12/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
#
# @timeTaken 16.661999940872192

from time import time
start = time()
print("Start time " + str(start))

remainder = True
smallestNumber = 0
while remainder:
	smallestNumber += 20
	for num in range(1,20):
		if smallestNumber % num != 0:
			break
		if num == 19:
			remainder = False



end = time()
print(smallestNumber)
print("Time taken " + str(end - start))


