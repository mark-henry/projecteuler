import primes

limit = 1000000

p = primes.Primes()
primes = list(p.allPrimesBelow(limit))
candidates = []
for index, prime in enumerate(primes):
	running_total = 0
	seq_length = 0
	while running_total < limit and index+seq_length < len(primes):
		if p.isPrime(running_total):
			candidates.append((seq_length, running_total))
			print (seq_length, running_total)
		running_total += primes[index + seq_length]
		seq_length += 1

print(max(candidates))