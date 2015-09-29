import itertools
import primes

p = primes.Primes()
ceiling = 50 * 10**6
numbers = set()
for first in itertools.takewhile(lambda x: x**2 < ceiling, p.iprimes()):
	for second in itertools.takewhile(lambda x: x < ceiling, p.iprimes()):
		if first**2 + second**3 > ceiling:
			break
		for third in itertools.takewhile(lambda x: x < ceiling, p.iprimes()):
			if first**2 + second**3 + third**4 > ceiling:
				break
			print(first, second, third)
			numbers.add(first**2 + second**3 + third**4)

print(len(numbers))