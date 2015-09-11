import primes, math

p = primes.Primes()

def oddComposites():
	current = 3
	while True:
		if not p.isPrime(current):
			yield current
		current += 2

def isDoubledSquare(num):
	if num % 2 != 0:
		return False
	sq = math.sqrt(num/2)
	return abs(sq - int(sq)) < 0.00001

def isgoldbachian(num):
	for prime in p.allPrimesBelow(num):
		if isDoubledSquare(num-prime):
				return True
	return False

for n in oddComposites():
	if not isgoldbachian(n):
		print n
		break