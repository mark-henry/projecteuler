import itertools

# The set of all possible arrangements of the numbers 1-9
onetonine = (''.join(seq) for seq in itertools.permutations('123456789'))
# The set of all possible arrangements of the numbers 0-9
zerotonine = (''.join(seq) for seq in itertools.permutations('0123456789'))