import itertools
from collections import Counter


# Utility functions
def value(card):
	return ''.join(card[:-1])

def suit(card):
	return card[-1]

def to_int(card):
	card_val = value(card)
	faces = {
		'A': 14,
		'K': 13,
		'Q': 12,
		'J': 11,
		'T': 10
	}
	if card_val in faces:
		return faces[card_val]
	else:
		return int(card_val)

def all_equal(iterable):
	return len(set(iterable)) <= 1


# Win-condition functions
def get_ofakind(hand, ofakind):
	'''Returns list of integer values of card values that appear
	at least ofakind times in this hand.'''
	counter = Counter(map(to_int, hand))
	return [value for value, count in counter.items() if count >= ofakind]

def get_pair(hand):
	return get_ofakind(hand, 2)

def get_two_pair(hand):
	pairs = get_ofakind(hand, 2)
	return pairs if len(pairs) == 2 else []

def get_three_kind(hand):
	return get_ofakind(hand, 3)

def has_straight(hand):
	hand = sorted(hand, key=to_int)
	for a, b in zip(hand[:-1], hand[1:]):
		if to_int(a) + 1 != to_int(b):
			return False
	return True

def has_flush(hand):
	return all_equal([suit(card) for card in hand])

def get_full_house(hand):
	'''Returns a list like [3, 2] for 3s full of 2s, or []'''
	three_kind = get_ofakind(hand, 3)
	if not three_kind:
		return []
	pairs = get_ofakind(hand, 2)
	house = three_kind
	house += [pair for pair in pairs if pair not in house]
	return house if len(set(house)) == 2 else []

def get_four_kind(hand):
	return get_ofakind(hand, 4)

def has_straight_flush(hand):
	return has_straight(hand) and has_flush(hand)

def has_royal_flush(hand):
	return has_flush(hand) and has_straight(hand) and \
		('A' in [value(card) for card in hand])


def high_card(hand1, hand2):
	'''Returns 0 if tie, 1 if hand1 has highest card,
		2 if hand2 has highest card.'''
	values1 = map(to_int, hand1)
	values2 = map(to_int, hand2)
	for card1, card2 in zip(sorted(values1, reverse=True), sorted(values2, reverse=True)):
		if card1 > card2:
			return 1
		if card1 < card2:
			return 2
	return 0


def winner(hand1, hand2):
	'''Returns 0 if tie, 1 if hand1 wins, 2 if hand2 wins.'''
	ranking = [has_royal_flush, has_straight_flush, get_four_kind, get_full_house, \
		has_flush, has_straight, get_three_kind, get_two_pair, get_pair]
	for condition in ranking:
		cond1 = condition(hand1)
		cond2 = condition(hand2)
		if cond1 > cond2:
			print "p1 wins by", condition.__name__
			return 1
		if cond2 > cond1:
			print "p2 wins by", condition.__name__
			return 2
	highest = high_card(hand1, hand2)
	print "player", highest, "wins by high card"
	return highest


def test():
	assert value('10H') == '10'
	assert value('AC') == 'A'
	assert to_int('AC') == 14
	assert to_int('10H') == 10
	assert to_int('QH') == 12
	assert to_int('2C') == 2
	assert [] == get_ofakind('5D 8C 9S JS AC'.split(), 2)
	assert [5] == get_ofakind('5H 5C 6S 7S KD'.split(), 2)
	assert [5, 6] == get_ofakind('5H 5C 6S 6S KD'.split(), 2)
	assert has_straight(['KH', 'JH', '10H', 'QH', 'AH'])
	assert has_royal_flush(['KH', 'JH', '10H', 'QH', 'AH'])
	assert get_full_house(['2H', '2D', '4C', '4D', '4S'])
	assert [5] == get_pair('5H 5C 6S 7S KD'.split())
	assert not get_pair(['5D', '8C', '9S', 'JS', 'AC'])
	assert 2 == winner('5H 5C 6S 7S KD'.split(), '2C 3S 8S 8D TD'.split())
	assert 1 == winner('5D 8C 9S JS AC'.split(), '2C 5C 7D 8S QH'.split())
	assert 2 == winner('2D 9C AS AH AC'.split(), '3D 6D 7D TD QD'.split())
	assert 1 == winner('4D 6S 9H QH QC'.split(), '3D 6D 7H QD QS'.split())
	fullhouse = ('2H 2D 4C 4D 4S'.split())
	assert [4, 2] == get_full_house(fullhouse)
	assert 1 == winner('2H 2D 4C 4D 4S'.split(), '3C 3D 3S 9S 9D'.split())


def main():
	matches = [line.split() for line in open('p054_poker.txt')]
	firstplayer_wins = 0
	for match in matches:
		hand1 = match[:5]
		hand2 = match[5:]
		print hand1, hand2
		if winner(hand1, hand2) == 1:
			firstplayer_wins += 1
	print "first player won", firstplayer_wins, "times"


if __name__ == '__main__':
	test()
	main()