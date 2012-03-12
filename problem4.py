from time import time

MIN_RANGE = 10000
MAX_RANGE = 998001

MAX_THREE_DIGIT_NUM = 999
MIN_THREE_DIGIT_NUM = 100

#Returns a list of palindromic numbers in range r1 to r2
def palindromicNumbers(r1,r2):
	numbers = []
	for num in range(r1,r2):
		if str(num) == str(num)[::-1]:
			numbers.append(num)

	return numbers


def findFacotrs(numbers):
	f1 = MAX_THREE_DIGIT_NUM
	f2 = 0
	for num in numbers[::-1]:
		f1 = MAX_THREE_DIGIT_NUM	
		while f1 > MIN_THREE_DIGIT_NUM:
			f2 = num % f1
			if f2 != 0 or (num/f1) > MAX_THREE_DIGIT_NUM or (num/f1) < MIN_THREE_DIGIT_NUM:
				f1 -= 1
			else:
				return(num)

		
start = time()
print("Start time " + str(start))
print(findFacotrs(palindromicNumbers(MIN_RANGE,MAX_RANGE)))
end = time()
print("Time taken " + str(end - start))