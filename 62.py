import itertools
import math
from collections import defaultdict
from collections import Counter


def explode_digits(n):
	digits = []
	while n:
		digits.append(n % 10)
		n /= 10
	return digits


cube_permutations = defaultdict(list)
for base in itertools.count(1):
	cube = base**3
	print cube
	digits = tuple(sorted(explode_digits(cube)))
	cube_permutations[digits].append(cube)
	if len(cube_permutations[digits]) == 5:
		print digits, cube_permutations[digits]
		break