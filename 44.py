import math
import itertools

def ispent(p):
	n = (1 + math.sqrt(24*p + 1)) / 6
	return abs(n - int(n)) < 0.00001

def pent(n):
	return n * (3*n - 1) / 2

def pent_pairs():
	for k in itertools.count(1):
		lower_bound = (math.sqrt(72*k - 47) + 1)
		lower_bound = max(int(lower_bound/6), 0)
		for j in range(lower_bound, k):
			yield (j, k)

for (j, k) in pent_pairs():
	pent_j, pent_k = pent(j), pent(k)
	if ispent(pent_j + pent_k) and ispent(pent_k - pent_j):
		print (j, k), (pent_j, pent_k), pent_k - pent_j
		exit()