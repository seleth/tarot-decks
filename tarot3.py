import random

def shuffle(deck):
	random.shuffle(deck)
	random.shuffle(deck)
	return deck

class card(suit, face):
	suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
	face = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Page', 'Knight', 'Queen', 'King']
print(suit, face)
