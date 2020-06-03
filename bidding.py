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

print ('\nGathering High Card Info')
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
		return ('Drunk')

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

## https://en.wikipedia.org/wiki/Bridge_Base_Basic#Opener_approximate_hand_strengths
def get_opening_bid():
	hcp = get_high_card_points()
	if get_balance() is 'Drunk':
		get_unbalanced_opening_bid(hcp)
	else:
		get_balanced_opening_bid(hcp)

## For unbalanced hands:
## 
## 0 - 12 points: Pass unless the hand is suitable for a preemptive opening bid.
## 13 - 21 points: Hands of 13 points or more are strong enough to open with natural bidding, including:
## minimum opening hands with 13-15 points
## medium opening hands with 16-18 points
## maximum opening hands with 19-21 points
## For unbalanced hands with 22+ points: show a very strong opening hand by using the strong 2♣ convention.

def get_unbalanced_opening_bid(hcp):
	print('Drunk Strategy')
	if hcp <= 12:
		print ('Pass')
	elif hcp <= 21:
		print ('wtf is natual bidding')
	elif hcp > 21:
		print ('Strong 2 Club Convention')


## For balanced hands, open with a no-trump bid when you can limit your hand to the following point ranges:
## 
## 1NT = 15-17 HCP
## 2NT = 20-21 HCP
## 3NT = 25-27 HCP
## For other balanced hands, you can still limit your points by opening in your longest suit and then using the no-trump bid on your second bid:
## 
## 13 - 14 HCP: bid 1 of a suit and then make a non-jump rebid in no trump (1NT)
## 18 - 19 HCP: bid 1 of a suit and then make a jump rebid in no trump (2NT)
## 22 - 24 HCP: bid 2♣ and then make a non-jump rebid in no trump (2NT)
## 28 - 30 HCP: bid 2♣ and then make a jump rebid in no trump (3NT)
## 31 - 32 HCP: bid 2♣ and then make a double-jump rebid in no trump (4NT)

def get_balanced_opening_bid(hcp):
	print ('TODO')

print('\nCrunching Numbers')
print ('============================')
print ('Balance: ', get_balance())
print ('HCP: ', get_high_card_points())
print ('TP: ', get_total_points())

print ('vhat to do, vhat to do....')
print ('============================')
print (get_opening_bid())

