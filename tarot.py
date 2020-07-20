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

selected_card1 = deck.pop(0)
selected_card2 = deck.pop(0)

spread = [selected_card1, selected_card2]

print(spread)

