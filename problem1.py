def problem1(maxN):
	print ( "Problem 1")
	sum = 0
	for i in range(0,maxN):
		if i % 3 == 0:
			#print(i)
			sum += i
		elif i % 5 == 0:
			#print(i)
			sum += i
	return sum

print( problem1(1000) )
