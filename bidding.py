#!/usr/bin/python3

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

class Hand:
	def __init__(self, suits, face_cards):
		self.suits = suits
		self.face_cards = face_cards

	## https://en.wikipedia.org/wiki/Bridge_Base_Basic#Opener_approximate_hand_strengths
	def get_opening_bid(self):
		hcp = self.get_high_card_points()
		if self.get_balance() is 'Drunk':
			return(self.get_unbalanced_opening_bid(hcp))
		else:
			return(self.get_balanced_opening_bid(hcp))

	def get_suit_counts(self):
		suit_counts = [self.suits['clubs'], self.suits['diamonds'], self.suits['hearts'], self.suits['spades']]
		suit_counts.sort()
		return suit_counts

	def get_balance(self):
		suits = tuple(self.get_suit_counts())
		if suits in balanced_hands:
			return (balanced_hands[suits])
		else:
			return ('Drunk')

	def get_high_card_points(self):
		return (
			(4 * self.face_cards['aces'])
		      + (3 * self.face_cards['kings'])
		      + (2 * self.face_cards['queens'])
		      + (1 * self.face_cards['jacks'])
		)

	def get_total_points(self):
		extra_points = 0
		for suit_count in self.get_suit_counts():
			if suit_count > 4:
				extra_points += suit_count - 4

		return self.get_high_card_points() + extra_points

	def get_unbalanced_opening_bid(self, hcp):
		if hcp <= 12:
			return 'Pass'
		elif hcp <= 21:
			return 'wtf is natual bidding'
		elif hcp > 21:
			return 'Strong 2 Club Convention'
		else:
			return ''


	def get_balanced_opening_bid(self, hcp):
		if hcp <= 12:
			return ('Pass')

		elif hcp >= 13 and hcp <= 14:
			return ('bid 1 of a suit and then make a non-jump rebid in no trump (1NT)')

		elif hcp >= 15 and hcp <= 17:
			return ('1NT')

		elif hcp >= 18 and hcp <= 19:
			return('bid 1 of a suit and then make a jump rebid in no trump (2NT)')

		elif hcp >= 20 and hcp <= 21:
			return ('2NT')

		elif hcp >= 22 and hcp <= 24:
			return('bid 2♣ and then make a non-jump rebid in no trump (2NT)')

		elif hcp >= 25 and hcp <= 27:
			return ('3NT')

		elif hcp >= 28 and hcp <= 30:
			return('bid 2♣ and then make a jump rebid in no trump (3NT)')

		elif hcp >= 31 and hcp <= 32:
			return('bid 2♣ and then make a double-jump rebid in no trump (4NT)')

		elif hcp > 21:
			return ('Strong 2 Club Convention')

		else:
			return None

def get_input():
	print ('Gathering Suit Info')
	print ('===================')

	clubs = int(input ('Clubs: '))
	diamonds = int(input ('Diamonds: '))
	hearts = int(input ('Hearts: '))
	spades = int(input ('Spades: '))

	sum = clubs + diamonds + hearts + spades
	if (sum is not 13):
		print ('Wrong number of cards, asshole.')

	suits = {}
	suits['clubs'] = clubs
	suits['diamonds'] = diamonds
	suits['hearts'] = hearts
	suits['spades'] = spades

	print ('\nGathering High Card Info')
	print ('============================')

	aces = int(input ('Aces: '))
	kings  = int(input ('Kings: '))
	queens = int(input ('Queens: '))
	jacks = int(input ('Jacks: '))

	face_cards = {}
	face_cards['aces'] = aces
	face_cards['kings'] = kings
	face_cards['queens'] = queens
	face_cards['jacks'] = jacks

	return Hand(suits, face_cards)

def main():
	hand = get_input()
	print('\nCrunching Numbers')
	print ('============================')
	print ('Balance: ', hand.get_balance())
	print ('HCP: ', hand.get_high_card_points())
	print ('TP: ', hand.get_total_points())

	print ('vhat to do, vhat to do....')
	print ('============================')
	#print (hand.get_opening_bid())

if __name__ == '__main__':
    main()
