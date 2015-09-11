def ispalindrome(num):
	tostring = str(num)
	for i in range(len(tostring)/2):
		if tostring[i] != tostring[(-i) - 1]:
			return False
	return True
	
largest = 0
for i in range(100, 1000):
	for j in range(100, i):
		if i * j > largest and ispalindrome(i * j):
			largest = i * j
			
print largest