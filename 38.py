import itertools
import pandigitals

n = 9  # The number of consecutive multipliers
largest = 0
while n > 2: 
	print 'n =', n
	multipliers = range(1, n+1)
	base = 1
	while True:
		concatenated_product = ''
		for m in multipliers:
			concatenated_product += str(m * base)
		if len(concatenated_product) > 9:
			break
		if concatenated_product in pandigitals.onetonine:
			print n, base, concatenated_product
			if int(concatenated_product) > largest:
				largest = int(concatenated_product)
		base += 1
	n -= 1

print '\nlargest was', largest