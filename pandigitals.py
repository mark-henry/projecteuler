import itertools

onetonine = map(''.join, set(itertools.permutations('123456789')))
zerotonine = map(''.join, set(itertools.permutations('0123456789')))