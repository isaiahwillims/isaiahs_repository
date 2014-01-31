import random

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# print letters 
# print '*********'
# hand = random.sample(letters, 6)
# print hand
# for i in hand:
# 	letters.remove(i)
# print '*********'
# print letters

hand_1 = []
hand_2 = []
hand_3 = []

for i in range(7):
	new_letter = random.choice(letters)
	letters.remove(new_letter)
	hand_1.append(new_letter)
	new_letter = random.choice(letters)
	letters.remove(new_letter)
	hand_2.append(new_letter)
	new_letter = random.choice(letters)
	letters.remove(new_letter)
	hand_3.append(new_letter)
	
	
print 'hand_1 %s' % hand_1
print 'hand_2 %s' % hand_2
print 'hand_3 %s' % hand_3

# print random.randrange(0, 100, 5)

# print random.sample(letters, 6)

# print random.random()

print 'Hello World'