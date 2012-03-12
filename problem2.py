fibNumber = []

def fibEvenSummation():
	sum = 0
	p1 = 0
	p2 = 1
	while p2+p1 < 4000000:
		p1 = p1 + p2
		p2 = p1 + p2
		
		if p1 % 2 == 0:
			sum += p1
		if p2 % 2 == 0:
			sum += p2

	return sum




print(fibEvenSummation())