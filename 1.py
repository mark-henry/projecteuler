def ismult(num, div):
	return num % div == 0
	
total = 0
for num in range(1000):
	if ismult(num, 3) or ismult(num,5):
		total += num
		
print total