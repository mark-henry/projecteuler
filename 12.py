import math

def divisors(n):
	for candidate in range(1, int(n/2)):
		if n % candidate == 0:
			yield candidate

def divisors_count(n):
	count = 0
	for candidate in range(1, int(math.sqrt(n))):
		if n % candidate == 0:
			count += 2
	return count

def triangles():
	i = 1
	sum = 0
	while True:
		sum += i
		i += 1
		yield sum

for triangle in triangles():
	print triangle, divisors_count(triangle)
	if divisors_count(triangle) > 500:
		exit()