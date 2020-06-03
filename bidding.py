#!/usr/bin/python3

print ('Gathering Suit Info')
print ('===================')

clubs = int(input ('Clubs: '))
diamonds = int(input ('Diamonds: '))
hearts = int(input ('Hearts: '))
spades = int(input ('Spades: '))

sum = clubs + diamonds + hearts + spades
if (sum is not 13):
	print ('Wrong number of cards, asshole.')

print ('\n\nGathering High Card Info')
print ('============================')

aces = int(input ('Aces: '))
kings  = int(input ('Kings: '))
queens = int(input ('Queens: '))
jacks = int(input ('Jacks: '))

## In the game of contract bridge, a balanced hand (or balanced distribution) 
## denotes a hand of thirteen cards which contains no singleton or void and 
## at most one doubleton. 
## Three hand patterns are classified as truly balanced: 4-3-3-3, 4-4-3-2 and 5-3-3-2. 
## The hand patterns 5-4-2-2 (an example of a two-suiter) 
## and 6-3-2-2 (a single-suiter) are generally referred to as semi-balanced.

balanced_hands = { 
	(3,3,3,4) : 'Truly',
	(2,3,4,4) : 'Truly',
	(2,3,3,5) : 'Truly',
	(2,2,4,5) : 'Semi',
	(2,2,3,6) : 'Semi'
}

def get_suits():
	suits = [clubs, diamonds, hearts, spades]
	suits.sort()
	return suits

def get_balance():
	suits = tuple(get_suits())
	if suits in balanced_hands:
		return (balanced_hands[suits])
	else:
		return ('Unbalanced. Tipsy as a drunk elf')


def get_high_card_points():
	return (
		(4 * aces) 
              + (3 * kings) 
              + (2 * queens) 
              + (1 * jacks)
        )

def get_total_points():
	extra_points = 0
	for suit_count in get_suits():
		if suit_count > 4:
			extra_points += suit_count - 4

	return get_high_card_points() + extra_points

print('\n\nCrunching Numbers')
print ('============================')
print ('Balance: ', get_balance())
print ('HCP: ', get_high_card_points())
print ('TP: ', get_total_points())
