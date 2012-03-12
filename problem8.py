def chunk(collection, chuckSize):
    return [collection[i:i+chuckSize] for i in range(0, len(collection), chuckSize)]

def printGridArray(array,width = 10):
	rows = chunk(array,width)
	print(" ")
	for row in rows:
		print(row)
	print(" ")



digits = []
with open("problem8.txt") as file:
    data = file.readlines()
    file.close()

for line in data:
	for digit in line.strip():
		digits.append(int(digit))

largest = -1
total = 1
index = 0
while index < len(digits)-5:
	
	total = digits[index ] * digits[index +1] * digits[index +2] * digits[index +3] * digits[index +4]

	if total > largest:
		largest = total

	index += 1


print(largest)

#printGridArray(digits,50)

