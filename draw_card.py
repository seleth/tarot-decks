import random

d = input("Enter the desired amount of cards pulled: ")
amnt = int(d)

print (amnt)

card = [
	('Ace of spades'),
	('Seven of clubs'),
	('King of diamonds'),
	('Nine of spades'),
	('Jack of hearts')
]

print(card)
deck = card.copy()

def draw(deck, amnt):
	while(amnt > 0):
		amnt += -1
		selected_card = deck.pop(0)
		print(selected_card)

draw(deck, amnt)
print(deck)
