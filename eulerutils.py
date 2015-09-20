import itertools


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


def is_palindrome(num):
	digits = explode_digits(num)
	for i in range(len(digits)/2):
		if digits[i] != digits[(-i) - 1]:
			return False
	return True


# ###
# Pandigitals
# The set of all possible arrangements of the numbers 1-9
onetonine = (''.join(seq) for seq in itertools.permutations('123456789'))
# The set of all possible arrangements of the numbers 0-9
zerotonine = (''.join(seq) for seq in itertools.permutations('0123456789'))


if __name__ == '__main__':
	print(explode_digits(123))
	print(implode_digits([1, 2, 3]))
