import primes

count = 0
iterations = 0
numerator = 3
denominator = 2
while True:
	numerator += denominator
	numerator, denominator = denominator, numerator
	numerator += denominator
	print numerator, denominator
	if len(str(numerator)) > len(str(denominator)):
		count += 1
	iterations += 1
	if iterations > 1000:
		break

print count