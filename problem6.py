sumOfSquares = 0
sumOfNumbers = 0
for n in range(0,101):
	sumOfSquares += n*n
	sumOfNumbers += n

print( sumOfNumbers*sumOfNumbers - sumOfSquares)