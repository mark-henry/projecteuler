import itertools
import math


cubes = set([1])
max_base = 1
max_cube = 1
def expand_cubes(new_max_cube):
	global cubes, max_cube, max_base
	while max_cube < new_max_cube:
		max_base += 1
		max_cube = max_base**3
		cubes.add(max_cube)
def is_cube(n):
	expand_cubes(n)
	return n in cubes


def digit_permutations_of(n):
	digits = []
	while n:
		digits.append(n % 10)
		n /= 10
	for p in itertools.permutations(digits):
		if p[0] == 0:
			continue
		number = 0
		for digit in p:
			number *= 10
			number += digit
		yield number


def count_solving_permutations(n):
	count = 0
	for p in set(digit_permutations_of(n)):
		if is_cube(p):
			count += 1
	return count


for base in itertools.count(1):
	count = count_solving_permutations(base**3)
	print base**3, count
	if count == 3:
		exit()