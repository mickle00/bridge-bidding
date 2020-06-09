#!/usr/bin/python3

import unittest
import bidding

class TestSum(unittest.TestCase):
	def test_high_card_points(self):
		hand = get_mock_hand([4,3,3,3], [3,3,3,3])
		hcp = hand.get_high_card_points()
		self.assertEqual(hcp, 30)

	def test_balanced_hands(self):
		balanced_hands = { 
			(3,3,3,4) : 'Truly',
			(2,3,4,4) : 'Truly',
			(2,3,3,5) : 'Truly',
			(2,2,4,5) : 'Semi',
			(2,2,3,6) : 'Semi'
		}
		for key, value in balanced_hands.items():
			hand = get_mock_hand(key, [3,3,3,3])
			balance = hand.get_balance()
			self.assertEqual(balance, value)

	def test_unbalanced_hands(self):
			hand = get_mock_hand([5,4,4,0], [3,3,3,3])
			balance = hand.get_balance()
			self.assertEqual(balance, 'Drunk')

def get_mock_hand(s, fc):
	suits = {}
	suits['clubs'] = s[0]
	suits['diamonds'] = s[1]
	suits['hearts'] = s[2]
	suits['spades'] = s[3]
	
	face_cards = {}
	face_cards['aces'] = fc[0]
	face_cards['kings'] = fc[1]
	face_cards['queens'] = fc[2]
	face_cards['jacks'] = fc[3]
	return bidding.Hand(suits, face_cards)
	
if __name__ == '__main__':
	unittest.main()
