def explode_digits(n):
	digits = []
	while n:
		digits.append(n % 10)
		n /= 10
	return digits

def implode_digits(digits):
	n = 0
	for d in digits:
		n *= 10
		n += d
	return n