def explode_digits(n):
	digits = []
	while n:
		digits = [n % 10] + digits
		n //= 10
	return digits

def implode_digits(digits):
	n = 0
	for d in digits:
		n *= 10
		n += d
	return n

if __name__ == '__main__':
	print(explode_digits(123))
	print(implode_digits([1, 2, 3]))