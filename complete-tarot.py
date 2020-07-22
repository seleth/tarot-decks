import random
import os

os.system('clear')

i = input("How many times to shuffle?: ")
d = input("How many cards to draw?: ")


draw_amnt = int(d)
times = int(i)

#shuffling mechanic
def shuffle(deck, times):
	for y in range(0, times):
		random.shuffle(deck)
		print('Shuffled one more time')



#drawing mechanic
def draw(deck, draw_amnt):
	cn = 1
	for x in range(0, draw_amnt):
		print('Card' + str(x))
		cn += 1
		selected_card = deck.pop(0)
		reverse_check = random.randint(0,1)
		if (reverse_check == 1):
			print('Reversed ' + selected_card[0] + selected_card[2])
		else:
			print(selected_card[0] + selected_card[1])



#cards of the deck
card =[
	('Ace of Wands: ', 'Creation, willpower, inspiration, desire', 'Lack of energy, lack of passion, boredom ', ''),
	('Two of Wands: ', 'planning, making decisions, leaving home', 'Fear of change, playing safe, bad planning'),
	('Three of Wands: ', 'Looking ahead, expansion, rapid growth', 'Obstacles, delays, frustration'),
	('Four of Wands: ', 'Sanctuary, community, home, celebration', 'Lack of support, transience, home conflicts', ''),
	('Five of Wands: ', 'competition, rivalry, conflict', 'Avoiding conflict, respecting differences', ''),
	('Six of Wands: ', 'victory, success, public reward' 'Excess pride, lack of recognition, punishment', ''),
	('Seven of Wands: ', ' perseverance, defensive, maintaining control', 'Give up, destroyed confidence, overwhelmed', ''),
	('Eight of Wands: ', 'Rapid action, movement, quick decisions', 'Panic, waiting, slowdown', ''),
	('Nine of Wands: ', ' resilience, grit, last stand', 'Exhaustion, fatigue, questioning motivations'),
	('Ten of Wands: ', 'Accomplishment, responsibility, burden', 'Inability to delegate, overstressed, burnt out', ''),
	('Page of Wands: ', 'Exploration, excitement, freedom'),
	('Knight of Wands: ', ' Action, adventure, fearlessness', 'Anger, impulsiveness, recklessness', ''),
	('Queen of Wands: ', 'Courage, determination, joy', 'Selfishness, jealousy, insecurities', ''),
	('King of Wands: ', 'Big picture, leader, overcoming challenges', 'Impulsive, overbearing, unachievable expectations'),

	('Ace of Cups: ', 'New feelings, spirituality, intuition', 'Emotional loss, blocked creativity, emptiness', ''),
	('Two of Cups: ', 'Unity, partnership, connection', 'Imbalance, broken communication, tension', ''),
	('Three of Cups: ', 'Friendship, community, happiness', 'Overindulgence, gossip, isolation', ''),
	('Four of Cups: ', 'Apathy, contemplation, disconnectedness', 'Sudden awareness, choosing happiness, acceptance', ''),
	('Five of Cups: ', 'Loss grief, self-pity', 'Acceptance, moving on, finding peace', ''),
	('Six of Cups: ', 'Familiarity, happy memories, healing', 'Moving forward, leaving home, independence', ''),
	('Seven of Cups: ', 'Searching for purpose, choices, daydreaming', 'Lack of purpose, diversion, confusion', ''),
	('Eight of Cups: ', 'Walking away, disillusionment, leaving behind', 'Avoidance, fear of change, fear of loss', ''),
	('Nine of Cups: ', 'Satisfaction, emotional stability, luxury', 'Lack of inner joy, smugness, dissatisfaction ', ''),
	('Ten of Cups: ', 'Inner happiness, fulfillment, dreams coming true', 'Shattered dreams, broken family, domestic harmony', ''),
	('Page of Cups: ', 'Happy surprise, dreamer, sensitivity', 'Emotional, Immaturity, insecurity, disappointment' ,''),
	('Knight of Cups: ', 'Following the heart, idealist, romantic', 'Moodiness, disappointment', ''),
	('Queen of Cups: ', 'Compassion, calm, comfort', 'Martyrdom, insecurity', ''),
	('King of Cups: ', 'Compassion, control, balance', 'Coldness, moodiness, bad advice', ''),

	('Ace of Swords: ', 'Breakthrough, clarity, sharp mind', 'Confusion, brutality, chaos', ''),
	('Two of Swords: ', 'Difficult choices, indecision, stalemate', 'Lesser of two evils, no right choice, confusion', ''),
	('Three of Swords: ', 'Heartbreak, suffering, grief', 'Recovery, forgiveness, moving on', ''),
	('Four of Swords: ', 'Rest, restoration, contemplation', 'Restlessness, burnout, stress', ''),
	('Five of Swords: ', 'Unbridled ambition, win at all costs, sneakiness', 'Lingering resentment, desire to reconcile, forgiveness', ''),
	('Six of Swords: ', 'Transition, leaving behind, moving on', 'Emotional baggage, unresolved issues, resisting transition', ''),
	('Seven of Swords: ', 'Deception, trickery, tactics and strategy', 'Coming clean, rethinking approach, deception', ''),
	('Eight of Swords: ', 'Imprisonment, entrapment, self-victimization', 'Self acceptance, new perspective, freedom', ''),
	('Nine of Swords: ', 'Anxiety, hopelessness, trauma', 'Hope, reaching out, despair', ''),
	('Ten of Swords: ', 'Failure, collapse, defeat', 'Cant get worse, only upwards, inevitable end', ''),
	('Page of Swords: ', 'Curiosity, restlessness, mental energy', 'Deception, manipulation, all talk', ''),
	('Knight of Swords: ', 'Action, impulsiveness, defending beliefs', 'No direction, disregard for consequences, unpredictability', ''),
	('Queen of Swords: ', 'Complexity, perceptiveness, clear mindedness', 'Cold hearted, cruel, bitterness', ''),
	('King of Swords: ', 'Head over heart, discipline, truth', 'Manipulative, cruel, weakness', ''),

	('Ace of Pentacles: ', 'Opportunity, prosperity, new venture', 'Lost opportunity, missed chance, bad investment', ''),
	('Two of Pentacles: ', 'Balancing decisions, priorities, adapting to change', '', ''),
	('Three of Pentacles: ', 'Teamwork, collaboration, building', 'Lack of teamwork, disorganized, group conflict', ''),
	('Four of Pentacles: ', 'Conservation, frugality, security', 'Greediness, stinginess, possessiveness', ''),
	('Five of Pentacles: ', 'Need, poverty, insecurity', 'Recovery, charity, improvement', ''),
	('Six of Pentacles: ', 'Charity, generosity, sharing', 'Strings attached, stinginess, power and domination', ''),
	('Seven of Pentacles: ', 'Hard work, perseverance, diligence', 'Work without results, distractions, lack of rewards', ''),
	('Eight of Pentacles: ', 'Apprenticeship, passion, high standards', 'Lack of passion, uninspired, no motivation', ''),
	('Nine of Pentacles: ', 'Fruits of labor, rewards, luxury', 'Reckless spending, living beyond means, false success', ''),
	('Ten of Pentacles: ', 'Legacy, culmination, inheritance', 'Fleeting success, lack of stability, lack of resources', ''),
	('Page of Pentacles: ', 'Ambition, desire, diligence', ' Lack of commitment, greediness, laziness', ''),
	('Knight of Pentacles: ', 'Efficiency, hard work, responsibility', 'Laziness, obsessiveness, work without reward', ''), 
	('Queen of Pentacles: ', 'Practicality, creature comforts, financial security', 'Self-centeredness, jealousy, smothering', ''),
	('King of Pentacles: ', 'Abundance, prosperity, security', 'Greed, indulgence, sensuality', ''),

	('0. The Fool: ', 'New beginnings, adventure, new challenges, oppourtunities that are often unplanned or unforseen', 'Missed oppourtunities, misadventure, unexpected problems, unrealistic goals, stupidity',  'Earth'),
	('I. The Magician: ', 'Strength of Will, the ability to apply intellect, correct decisions, balance and harmony', 'Indecisiveness, lack of will power, weak intellect, arrogance, false knowledge', '(Aries)'),
	('II. The High Priestess: ', 'Intuition, inspiration, revelation, psychic and artistic ability, hidden knowledge', 'Emotional unstability, hypocrisy, fickleness, narrow vision', '(Taurus'),
	('III. The Empress: ', 'Wealth, abundance, fertility, growth, motherhood, pregnancy, physical creativity', 'Infertility, lack of creativity, poverty', '(Gemini)'),
	('IV. The Emperor: ', 'Masculine power,leadership, authority, benevolence, stability, protection, realization, a great person', 'Dictatorship, oppression, powerlessness, immaturity, injury due to anothers action, fraud', 'Cancer'),
	('V. The Hierophant: ', 'Religion, ritual, conformity, orthodoxy, captivity, servitude, one who gives spiritual advice, marriage', 'Spiritual Creativity, openness to new ideas, invention, Bohemian attitudes, idealism', 'Leo'),
	('VI. The Lovers: ', 'Choice, attraction, love, beauty, temptation, mental and spiritual harmony, marriage', 'Quarrelling, infidelity, broken marriage, unstable emotions, indecision', 'Virgo'),
	('VII. The Chariot: ', 'Triumph, victory, success, control over natural forces, balance', 'Unethical victory, decadance, ill health, restlessness and desire for change', 'Libra'),
	('VIII. Justice: ', 'Justice, balance, equality, equity, law, triumph, good decision making, spiritual growth', '', 'Aquarius'),
	('IX. The Hermit: ', 'SIlent counsel, prudence, discretion, recieving Divine wisdom, expert advice, the guidel, the teacher', 'Ignorance, immaturity, foolishness, vices', 'Sagittarius'),
	('X. The Wheel of Fortune: ', 'Success, unexpected luck, change of fortune, chance, evolution, ebb and flow', 'Failure, setbacks, reap as you sow, poverty, stagnation', 'Capricorn'),
	('XI. Strength: ', 'Strength, courage, force of character, love over hate, spiritual over material', 'Abuse of power, domination of material things, discord, lack of moral force', 'Scorpio'),
	('XII. The Hanged Man: ', 'Wisdom, spirituality, prophetic powers, hiatus, life suspended, transformation of personality', 'Arrogance, preoccupation, ego, materialism, resistance to spirituality, flase prophecy', 'Pisces'),
	('XIII. Death: ', 'The end, positive change, transformation, renewal, rebirth, new ideas, new oppourtunities', 'Disaster, inertia, revolution, anarchy, upheaval, political change', 'Saturn'),
	('XIV. Temperance: ', 'Adaptation, tempering, coordination, cooperation, cooperation, self-control, moderation, harmony, good management', 'Competing interests, unfortunate combinations, arguments, corruption, seperation, bad advice', 'Mercury'),
	('XV. The Devil: ', 'Discontent, depression, illness, misuse of force, materialism, ignorance, over indulgence, negative magic', 'Spiritual understanding, overcoming materialism, indecisiveness, alturism, selflessness', 'Mars'),
	('XVI. The Tower: ', 'Change, conflict, destruction, disruption, enlightenment, failure, backruptcy', 'Gain at great cost, flase accusations, false imprisonment, oppression', 'Uranus'),
	('XVII. The Star: ', 'Insight, inspiration, hope, selflessness, good health, spiritual gifts, great love', 'Pessimism, doubt, stubbornness, lack of perception, illness', 'Venus'),
	('XVIII. The Moon: ', 'Intuition, imagination, psychic abilities, creativity, the occult', 'Illusion, deception, loss by crime, bad luck unforseen perils', 'Moon'),
	('XIX. The Sun: ', 'Material happiness, success, attainment, achievements in arts and sciences, good marriage, happy reunions', 'Uncertainty, marriage, problems, health problems, loss of job or home, unhappiness, depression', 'Sun'),
	('XX. The Last Judgment: ', 'Awakening, renewal, legal judgements in ones favor, change in consciousness', 'Weakness, disillusion, fear of death, unhappiness, seperation, divorce, material loss', 'Jupiter'),
	('XXI. The World: ', 'Completion, reward, success, triumph, travel, liberation', 'Success yet to be won, fear of change or travel, over-attachment, lack of vision', 'Neptune')
]


#setting deck
deck = card.copy()

#shuffling the deck
shuffle(deck, times)

draw(deck, draw_amnt)

#OLD MECHANIC GRAVE YARD R.I.P.=--------------------------------------------

#checking for reverses and printing
#print('Past')
#Past = deck.pop(0)
#past_reverse = random.randint(0,1)
#if (past_reverse == 1):
#	print(Past[0] + Past[2])
#else:
#	print(Past[0] + Past[1])

#print('Present')
#Present = deck.pop(0)
#present_reverse = random.randint(0,1)
#if (present_reverse == 1):
#	print(Present[0] + Present[2])
#else:
#	print(Present[0] + Present[1])

#print('Future')
#Future = deck.pop(0)
#future_reverse = random.randint(0,1)
#if (future_reverse == 1):
#	print(Future[0] + Future[2])
#else:
#	print(Future[0] + Future[1])

