import random

card =[
	('Ace of Spades'),
	('Seven of Clubs'),
	('King of Diamonds'),
	('Nine of spades'),
	('Jack of Hearts')
]

deck = card.copy()

random.shuffle(deck)

selected_card = deck.pop(0)

print(selected_card)
