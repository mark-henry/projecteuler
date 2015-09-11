import pandigitals

divisors = [2, 3, 5, 7, 11, 13, 17]
def isinteresting(p):
	for index in range(1, 8):
		if not (int(p[index:index+3]) % divisors[index - 1] == 0):
			return False
	return True

total = 0
for p in pandigitals.zerotonine:
	if isinteresting(p):
		total += int(p)

print total