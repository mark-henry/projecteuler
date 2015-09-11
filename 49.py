import primes
from itertools import *

p = primes.Primes()

def oddfourdigitnumbers():
	for i in range(1000, 10000, 2):
		yield str(i)

def issequence(integers):
	gap1 = integers[1] - integers[0]
	gap2 = integers[2] - integers[1]
	return gap1 == gap2 and gap1 != 0

def fourdigits(integers):
	return all(num > 1000 and num < 10000 for num in integers)

def areprime(integers):
	return all(p.isPrime(num) for num in integers)

winners = []
for n in oddfourdigitnumbers():
	for triad in combinations(permutations(n), 3):
		triad = [int(''.join(num)) for num in triad]
		triad.sort()
		if fourdigits(triad) and issequence(triad) and areprime(triad):
			winners += triad

print set(winners)