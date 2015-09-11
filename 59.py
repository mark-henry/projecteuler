import csv, itertools

cipher = open('p059_cipher.txt', 'r').read()

letters = 'abcdefghijklmnopqrstuvwxyz'
def possible_keys():
	for first in letters:
		for second in letters:
			for third in letters:
				yield [ord(first), ord(second), ord(third)]

def decode(ciphertext, key):
	result = ""
	keyiter = itertools.cycle(key)
	for c in ciphertext:
		result += chr(c ^ next(keyiter))
	return result

with open('p059_cipher.txt') as csvfile:
	ciphertext = map(int, list(csv.reader(csvfile))[0])
	for key in possible_keys():
		plaintext = decode(ciphertext, key)
		if 'the' in plaintext and ' a ' in plaintext:
			print plaintext
			print ''.join([chr(s) for s in key])
			print sum([ord(c) for c in plaintext])
