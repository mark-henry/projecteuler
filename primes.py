class Primes(object):
	def __init__(self):
		self.size = 4
		self.primes = [2, 3]
		self.factorizations = {2:[2], 3:[3], 4:[2,2]}

	def primeFactors(self, number):
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
		return number in self.primes

	def expand(self, request):
		while self.size <= request:
			newsize = self.size * 2
			sieve = [True] * (newsize - self.size)
			#Apply existing primes to sieve
			#Simultaneously expand factorizations
			for prime in self.primes:
				factor = 2
				while factor*prime < self.size:
					factor += 1
				while factor*prime < newsize:
					sieve[factor*prime - self.size] = False
					self.factorizations[factor*prime] = \
						[prime] + self.primeFactors(factor)
					factor += 1
			#Collect new primes
			for i in range(len(sieve)):
				if sieve[i] == True:
					newprime = i + self.size
					self.primes += [newprime]
					self.factorizations[newprime] = [newprime]
			self.size = newsize

	def allPrimesBelow(self, number):
		self.expand(number)
		position = 0
		length = len(self.primes)
		while position < length and self.primes[position] < number:
			yield self.primes[position]
			position += 1

	def primes(self):
		position = 0
		while True:
			self.expand(position)
			yield self.primes[position]
			position += 1