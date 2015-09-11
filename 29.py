import pandigitals

products = []
for p in pandigitals.onetonine:
	for multplace in range(1, 8):
		for eqplace in range(multplace+1, 9):
			term1 = int(p[:multplace])
			term2 = int(p[multplace:eqplace])
			product = int(p[eqplace:])
			if term1 * term2 == product:
				products += [product]
				print "%s x %s = %s" % (term1, term2, product)

print "Sum of products is", sum(set(products))