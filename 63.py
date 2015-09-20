import itertools


def for_n_equals(power):
	lower = 10**(power-1)
	upper = 10**power
	base = 1
	count = 0
	while base**power < upper:
		if base**power >= lower:
			print(base**power)
			count += 1
		base += 1
	return count


# Why is this the limit? I couldn't tell you, I'm very tired right now
power_limit = 22
total = sum([for_n_equals(n) for n in range(1, power_limit)])
print(total)
