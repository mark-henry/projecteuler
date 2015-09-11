
def isevendiv(cand):
	for i in range(2, 21):
		if cand % i != 0:
			return False
	return True
	
def findevendiv():
	cand = 20
	while True:
		cand += 20
		if isevendiv(cand):
			return cand

print findevendiv()