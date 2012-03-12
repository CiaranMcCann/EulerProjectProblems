from time import time
start = time()
print("Start time " + str(start))

remainder = True
smallestNumber = 0
while remainder:
	smallestNumber += 20
	#print(smallestNumber)
	for num in range(1,20):
		if smallestNumber % num != 0:
			break
		if num == 19:
			remainder = False



end = time()
print(smallestNumber)
print("Time taken " + str(end - start))


