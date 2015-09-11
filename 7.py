primes = [2]
cand = 3

def isprime(num):
	for prime in primes:
		if num % prime == 0:
			return False
	return True
	
while len(primes) < 10001:
	cand += 2
	if isprime(cand):
		primes += [cand]
		
print primes[-1]