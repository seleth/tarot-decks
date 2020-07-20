import random

def shuffle(deck):
	random.shuffle(deck)
	random.shuffle(deck)
	return deck


#cards of the deck
card = [
	('Ace of Swords: ', 'Protection', ''),
	('Page of Cups: ', 'Passionate youth', ''),
	('The Tower: ', 'Sudden destructive change', ''),
	('The Fool: ', 'Unlimited potential', ''),
	('Death: ', 'Positive change', ''),
	('Four of Wands: ', 'Sancutary', ''),
	('Five of Pentacles: ', 'Illness', ''),
	('The Moon: ', 'Intuition', ''),
	('Wheel of Fortune: ', 'Change of luck', ''),
	('Nine of Swords: ', 'Sorrow', ''),
	('Hierophant: ', 'Spiritual conformity', ''),
	('Four of Cups: ', 'Emotionally unrest', ''),
	('Five of Cups:', 'Fit of rage', ''),
	('The World: ', 'Success', ''),
	('Eight of Wands: ', 'Movement in a situation', ''),
	('Ten of Wands: ', 'Oppression', ''),
	('Eight of Swords: ', 'Indecision/ Inaction', ''),
	('Seven of Swords: ', 'Failing plan', ''),
	('Two of Swords: ', 'Harmony', '')
]

#setting deck
deck = card.copy()

#shuffling the deck
shuffle(deck)



#checking for reverses and printing
print('Past')
Past = deck.pop(0)
past_reverse = random.randint(0,1)
if (past_reverse == 1):
	print(Past[0] + Past[2])
else:
	print(Past[0] + Past[1])

print('Present')
Present = deck.pop(0)
present_reverse = random.randint(0,1)
if (present_reverse == 1):
	print(Present[0] + Present[2])
else:
	print(Present[0] + Present[1])

print('Future')
Future = deck.pop(0)
future_reverse = random.randint(0,1)
if (future_reverse == 1):
	print(Future[0] + Future[2])
else:
	print(Future[0] + Future[1])

