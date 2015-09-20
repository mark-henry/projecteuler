import primes
import math
import itertools
from eulerutils import *

p = primes.Primes(False)


def replace(exploded, replace_mask, digit):
	return [digit if replace else original for replace, original in zip(replace_mask, exploded)]

for n in p.iprimes():
	exploded = explode_digits(n)
	for replace_mask in itertools.product([True, False], repeat=len(exploded)):
		prime_count = 0
		fails_count = 0
		for digit in range(1, 10):
			replaced = implode_digits(replace(exploded, replace_mask, digit))
			if p.isPrime(replaced):
				prime_count += 1
				print(n, "sub", digit, "becomes", replaced, "for", prime_count)
			else:
				fails_count += 1
				if fails_count == 3:
					break  # Short-circuit the search if we can't possibly make it to 8
		if prime_count == 8:
			exit()