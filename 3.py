import math

def isprime(num):
	for check in range(2, int(math.sqrt(num))+1):
		if num % check == 0:
			return False
	return True

def getfactors(num):
	facts = []
	for cand in range(2, int(math.sqrt(num))+1):
		if num % cand == 0 and isprime(cand):
			facts += [cand]
	return facts

facts = getfactors(600851475143)
print max(facts)