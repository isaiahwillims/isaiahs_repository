#!!!!!How do I thread a dictionary into a dictionary?!!!!!

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# magic_cards = {'Witchstalker':{'Cost':'1GG', 'Type':'Creature — Wolf', 'Pow/Tgh':'(3/3)', 
#                                'Rules Text':'''Hexproof (This creature can't be the target of spells or abilities your opponents control.)
# Whenever an opponent casts a blue or black spell during your turn, put a +1/+1 counter on Witchstalker.''',
#                                 'Set/Rarity': 'Magic 2014 Core Set Rare'},
#                 'Woodborn Behemoth': } 

#
cardname = {}
cardstat = {}

file = open('magic_cards.txt', 'U')
for line in file:
	card_info = line.split('\t')
	if card_info[0] == 'Name': 
		cardname[card_info[1]] = card_info[1]
	elif card_info[0] == 'Cost:':
		cardstat['cost'] = card_info[1]
	elif card_info[0] == 'Type:':
		cardstat['type'] = card_info[1]
	elif card_info[0] == 'Pow/Tgh:':
		cardstat['P/T'] = card_info[1]
	elif card_info[0] == 'Rules Text:':
		cardstat['Efects'] = card_info[1]
	elif card_info[0] == 'Set/Rarity:':
 		cardstat['Set/Rarity'] = card_info[1]

#for entry in cardstat:
#	cardname[cardstat['cost']]

#file = open('magic_cards.txt', 'U')
#for line in file: #isn't working
#	card_name = line.split('\t') # It adds nothing to dictionary
#	if card_name[0] == 'Name:': #
#		mtgcards['name'] = card_name[1]	#
print "**********************"
print cardstat
print "**********************"
print cardname

#     name = line.split('\t')[1]
#     cards[name] = card_info

# 
# cards = {}
# card_info = {}
# #Add an item to a dictionary
# cards['key'] = 'value'
# card_info['Cost'] = '1R' 
# cards['Dragon Hatchling'] = card_info
# 
# file = open('file_name', 'U')
# 
# def get_card_dictionary(file):
#     for line in file:
#     return card_dictionary