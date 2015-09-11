import primes

p = primes.Primes()

log = []
def report(integer):
	global log
	if log != [] and integer != log[-1] + 1:
		log = []
	log += [integer]
	if len(log) == 4:
		print log
		exit()

def naturals():
	n = 1
	while True:
		yield n
		n += 1

for n in naturals():
	facts = p.distinctPrimeFactors(n)
	if len(facts) == 4:
		report(n)