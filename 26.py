#Not strictly correct
def cyclelength(number):
	current = 10
	history = []
	while True:
		history += [current]
		factor = int(current/number)
		current -= factor*number
		current *= 10
		if current in history:
			break
	return len(history)

print cyclelength(1)
print cyclelength(6)
print cyclelength(7)

longest = (0, 0)
for number in range(1, 1000):
	print "examining %s" % number
	length = cyclelength(number)
	if length > longest[1]:
		longest = (number, length)

print "%s has the longest cycle with a length of %s" % longest