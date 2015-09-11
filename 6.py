def sumsquares(count):
	sum = 0
	for i in range(1, count+1):
		sum += i*i
	return sum
	
def squaresum(count):
	sum = 0
	for i in range(1, count+1):
		sum += i
	return sum*sum

print squaresum(100) - sumsquares(100)