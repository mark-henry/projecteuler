#lel
print sum(map(int, str(2**1000)))

#OK this time for real
digits = [1] + ([0] * 500)
for i in range(1000):
	prevremainder = 0
	for i in range(len(digits)):
		nextremainder = int(((digits[i] * 2) + prevremainder)/ 10)
		digits[i] = ((digits[i] * 2) + prevremainder) % 10
		prevremainder = nextremainder

print sum(digits)