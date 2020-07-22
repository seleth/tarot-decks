import random

i = input("Enter amount of times to shuffled(Default:1): ")
amnt = int(i)

print(amnt)

card = [
	('Ace of spades'),
	('Seven of clubs'),
	('King of diamonds'),
	('Nine of spades'),
	('Jack of hearts')
]

print(card)
deck = card.copy()

def shuffle(deck, amnt):
	for x in range(0, amnt):
		random.shuffle(deck)
		print('Shuffled')

shuffle(deck, amnt)

print (deck)
