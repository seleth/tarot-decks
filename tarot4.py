import random

def shuffle(deck):
	random.shuffle(deck)
	random.shuffle(deck)
	return deck

class Card:
	def __init__(self, suit, meaning, r_meaning):
		self.suit = card
		self.meaning = card[0,1]
		self.r_meaning = card[0,2]




card = [
	('card1: ', 'A', 'B'),
	('card2: ', 'A', 'B'),
	('card3: ', 'A', 'B'),
	('card4: ', 'A', 'B')
]

deck = card.copy()

Selected_card = deck.pop(0)



rev = random.randint(0,1)
if (rev == 1):
	print(Selected_card[0] + Selected_card[2])
else:
	print(Selected_card[0] + Selected_card[1])
