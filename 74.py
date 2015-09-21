from eulerutils import *
import math


chains_memo = {}
def factorial_chain(num, prev_chain=[]):
	'''
	Returns list representing factorial chain starting from num, including num.
	Chain ends before first recurrence of number that is already in the chain.
	'''
	if num in chains_memo:
		return chains_memo[num]
	next_num = sum([math.factorial(digit) for digit in explode_digits(num)])
	if next_num in prev_chain:
		return [num]
	chain = [num] + factorial_chain(next_num, prev_chain + [num])
	chains_memo[num] = chain
	return chain


count = 0
for starting_num in range(1000000):
	if len(factorial_chain(starting_num)) == 60:
		count += 1
print(count)