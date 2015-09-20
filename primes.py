import bisect, math

class Primes(object):
	def __init__(self, track_factorizations=True):
		self.size = 4
		self.primes = [2, 3]
		self.factorizations = {2:[2], 3:[3], 4:[2,2]}
		self.track_factorizations = track_factorizations

	def primeFactors(self, number):
		if not self.track_factorizations:
			raise ValueError("Not tracking factorizations")
		if number < 2:
			return []
		self.expand(number)
		return self.factorizations[number]

	def distinctPrimeFactors(self, number):
		return set(self.primeFactors(number))

	def isPrime(self, number):
		if number < 2:
			return False
		self.expand(number)
		index = bisect.bisect_left(self.primes, number)
		return index != len(self.primes) and self.primes[index] == number

	def expand(self, request=None):
		if request is None:
			request = self.size * 2
		while self.size < request:
			newsize = self.size * 2
			sieve = {}
			#Apply existing primes to sieve
			#Simultaneously expand factorizations
			for prime in self.primes:
				factor = math.ceil(self.size / prime)
				while factor*prime < newsize:
					sieve[factor*prime] = True
					if self.track_factorizations:
						self.factorizations[factor*prime] = \
							[prime] + self.primeFactors(factor)
					factor += 1
			#Collect new primes
			for candidate_prime in range(self.size+1, newsize, 2):
				if candidate_prime not in sieve:
					self.primes.append(candidate_prime)
					self.factorizations[candidate_prime] = [candidate_prime]
			self.size = newsize

	def allPrimesBelow(self, number):
		self.expand(number)
		position = 0
		length = len(self.primes)
		while position < length and self.primes[position] < number:
			yield self.primes[position]
			position += 1

	def iprimes(self):
		position = 0
		last = 0
		while True:
			if position == len(self.primes):
				print("ech")
				self.expand()
			last = self.primes[position]
			yield last
			position += 1

	def next_prime(self, prev):
		index = 0
		self.expand(prev)
		while True:
			index = bisect.bisect_left(self.primes, prev)
			if (index + 1) >= len(self.primes):
				self.expand()
			if self.primes[index] >= prev:
				return self.primes[index + 1]

if __name__ == "__main__":
	p = Primes(False)
	for number in range(10):
		print(number, "is followed by", p.next_prime(number))
	assert not p.isPrime(9)
	assert p.isPrime(13)
	assert p.isPrime(17)
	assert p.isPrime(31)
	assert p.isPrime(43)
	for index, prime in enumerate(p.iprimes()):
		print(index, prime)
		if index > 10:
			break