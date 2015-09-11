import math

def numsolutions(p):
	count = 0
	for a in range(1, int(p/2)):
		for b in range(a, p):
			c = p - a - b
			if abs(c - math.sqrt(a**2 + b**2)) < 0.0001:
				count += 1
	return count

greatest = (0,0)
for p in range(2, 1000, 2):
	count = numsolutions(p)
	if count > greatest[1]:
		greatest = (p, count)

print greatest