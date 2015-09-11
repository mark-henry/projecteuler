import math
import Queue

def ispent(p):
	n = (1 + math.sqrt(24*p + 1)) / 6
	return abs(n - int(n)) < 0.00001

def pent(n):
	return n * (3*n - 1) / 2

def cheapestunexamined():
	largestYet = 0
	pq = Queue.PriorityQueue()
	pq.put((pent(2) - pent(1), 1, 2))
	while True:
		(cost, a, b) = pq.get()
		pq.put((pent(b+1) - pent(a+1), a+1, b+1))
		if b - a > largestYet:
			largestYet = b - a
			pq.put((pent(b+1) - pent(a), a, b+1))
		yield (a, b)

for (a, b) in cheapestunexamined():
	if ispent(pent(a) + pent(b)) and ispent(pent(b) - pent(a)):
		print "%s and %s; difference %s" % (pent(a), pent(b), pent(b) - pent(a))
		exit()