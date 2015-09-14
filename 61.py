import itertools
import math


# Oracles
def first_two_digits(n):
	return n // 100
def last_two_digits(n):
	return n % 100
def is_consistent(first, second):
	return last_two_digits(first) == first_two_digits(second)

def is_internally_cyclic(theSet):
	for first, second in zip(theSet[:-1], theSet[1:]):
		if not is_consistent(first, second):
			return False
	return True

def is_cyclic(theSet):
	return is_internally_cyclic and is_consistent(theSet[-1], theSet[0])


# Generators
def four_digit_polygonals(s):
	def P(n):
		return (n*n * (s - 2) - n * (s - 4)) / 2
	polygonals = (P(n) for n in itertools.count(1))
	return itertools.takewhile(lambda n: n < 10000,
		itertools.dropwhile(lambda n: n < 1000, polygonals))


# Traversal and control
def special_cyclic_sets(polygonality_list):
	if not polygonality_list:
		yield []
		return

	tails = list(special_cyclic_sets(polygonality_list[1:]))
	for number in four_digit_polygonals(polygonality_list[0]):
		for tail in tails:
			candidate_set = [number] + tail
			if is_internally_cyclic(candidate_set):
				yield candidate_set


# Driver
for polygonalities in itertools.permutations(range(3,9), 6):
	for s in special_cyclic_sets(polygonalities):
		if is_cyclic(s):
			print s, sum(s)