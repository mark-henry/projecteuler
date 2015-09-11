max = 2000000
isprime = [True] * max

def nextprime(current):
	current += 1
	while current < max and not isprime[current]:
		current += 1
	return current

sieve = 2
while sieve < max:
	i = 2
	while i*sieve < max:
		isprime[i * sieve] = False
		i += 1
	sieve = nextprime(sieve)
	
sum = 0
for number in range(2, len(isprime)):
	if isprime[number]:
		sum += number
	
print sum