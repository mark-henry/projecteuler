import primes, sys

p = primes.Primes()
most = (-1000, -1000, 0)

a = -1000
while a < 1000:
	a += 1
	b = -1000
	while b < 1000:
		b += 1
		n = 0
		while p.isPrime(n*n + a*n + b):
			n += 1
		if n > most[2]:
			most = (a, b, n)

print most
print most[0] * most[1]