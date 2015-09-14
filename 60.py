import math
import primes
import itertools

p = primes.Primes()

set_size = 4

def solutions():
	return itertools.permutations(p.allPrimesBelow(674), set_size)

# for solution in solutions():
# 	print(solution)

def concatenate(first, second):
	digits = 1 + int(math.log(second, 10))
	result = first * int(math.pow(10, digits)) + second
	return result

def is_solution(solution):
	for pair in itertools.permutations(solution, 2):
		if not p.isPrime(concatenate(pair[0], pair[1])):
			return False
	return True

for solution in solutions():
	print(solution)
	if is_solution(solution):
		print("solution:", sum(solution), solution)
		break