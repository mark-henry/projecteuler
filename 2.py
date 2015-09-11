fibs = [1, 1]

#Generate fibs
while fibs[-1] < 4000000:
	fibs += [fibs[-1] + fibs[-2]]

total = 0
for num in fibs:
	if num % 2 == 0:
		total += num
		
print total