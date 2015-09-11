import primes

p = primes.Primes()
ps = list(p.allPrimesBelow(1000000))
candidates = []
for index in range(len(ps)):
	total = 0
	offset = 0
	while total < 1000000:
		total += ps[index + offset]
		offset += 1
		if p.isPrime(total):
			candidates += [(total, offset)]
			print (total, offset)

print max(candidates)