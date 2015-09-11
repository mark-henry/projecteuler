longest = (1, 0)
cache = { 1: 0 }

def seqlength(startnumber):
	if startnumber in cache:
		return cache[startnumber]
	history = []
	n = startnumber
	while not n in cache:
		history += [n]
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
	count = cache[n] 
	for prev in history[::-1]:
		count += 1
		cache[prev] = count
	cache[startnumber] = count
	return count

for startnumber in range(1, 1000000):
	length = seqlength(startnumber)
	if length > longest[1]:
		longest = (startnumber, length)
		
print "%s is the longest, with a seqlength of %s" % (longest[0], longest[1])