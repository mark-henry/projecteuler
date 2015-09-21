import itertools


def three_groups(solution):
	yield solution[:3]
	for start_index in [3, 5, 7]:
		yield [solution[i] for i in (start_index, start_index-1, start_index+1)]
	yield [solution[i] for i in (-1, -2, 1)]


numbers = list(range(1, 11))
solutions = []
for soln in itertools.permutations(numbers):
	groups = list(three_groups(soln))
	# Enforce start with numerically lowest external node
	if min([group[0] for group in groups]) is not soln[0]:
		continue
	# Enforce common sum
	sums = [sum(group) for group in groups]
	if len(set(sums)) > 1:
		continue
	solutions.append(groups)

winner = max(solutions)
print(winner)