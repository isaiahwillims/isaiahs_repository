#!/usr/bin/env python
# -*- coding: utf-8 -*-

cardname = {}
cardstat = {}

file = open('magic_cards.txt', 'U')
#def get_card_dictionary(file):
for line in file:
    card_info = line.strip().split('\t')
    if len(card_info) < 2:
        continue
    if card_info[0] == 'Name': 
        cardname[card_info[1]] = {}
        cardstat = cardname[card_info[1]]
        cardstat['Name'] = card_info[1]
    elif card_info[0] == 'Cost:': #and len(card_info) == 2:
        cardstat['cost'] = card_info[1]
    elif card_info[0] == 'Type:':
        cardstat['type'] = card_info[1]
    elif card_info[0] == 'Pow/Tgh:': #and len(card_info) == 2:
        cardstat['P/T'] = card_info[1]
    elif card_info[0] == 'Rules Text:': #and len(card_info) == 2:
        cardstat['Efects'] = card_info[1]
    elif card_info[0] == 'Set/Rarity:':
        cardstat['Set/Rarity'] = card_info[1]

#print "***************************************************"            
#print cardname
print "***************************************************"

#cards, values = cardname.items()

#add a card to the end of a list
#cards.append(card)
#insert a card into a specific place in the deck
#cards.insert(0, card)
#remove the last card form the deck and return it
#cards.pop()

################

#open('magic_decks.py','U')

#Red_Blue_Burst = [cardname['Divination'], cardname['Divination'], cardname['Divination\n'], cardname['Divination\n'], cardname['Shock\n'], cardname['Shock\n'], cardname['Shock\n'], cardname['Shock\n'], cardname['Cancel\n'], cardname['Cancel\n'], cardname['Cancel\n'], cardname['Cancel\n'], cardname['Molten Birth\n'], cardname['Molten Birth\n'], cardname['Molten Birth\n'], cardname['Molten Birth\n'], cardname['Young Pyromancer\n'], cardname['Young Pyromancer\n'], cardname['Young Pyromancer\n'], cardname['Young Pyromancer\n'], cardname['Disperse\n'], cardname['Disperse\n'], cardname['Disperse\n'], cardname['Disperse\n'], cardname['Wild Guess\n'], cardname['Wild Guess\n'], cardname['Wild Guess\n'], cardname['Wild Guess\n'], cardname['Archaeomancer\n'], cardname['Archaeomancer\n'], cardname['Archaeomancer\n'], cardname['Archaeomancer\n'], cardname['Colossal Whale\n'], cardname['Colossal Whale\n'], cardname['Ogre Battledriver\n'], cardname['Ogre Battledriver\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Mountain\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n'], cardname['Island\n']]

#deck = ['Cancel\n' * 3, 'Divination\n' * 5]

#Basic = [cardname['Mountain'] ,cardname['Island'], cardname['Plains'], cardname['Forest'], cardname['Swamp']]

basic = ['Mountain', 'Island', 'Plains', 'Forest', 'Swamp']

legal = ['1', '2', '3', '4']

deck = open('Red_Blue_Burst.Deck', 'U')
#def deck_list_reader(deck):
for line in deck:
    card = line.strip().split('\t')
    if card[0] == basic:
        continue
    if card[1] == legal:
        print "Deck valid :)"
    else:
        print "!!!Deck not valid!!!"

print "*" * 50
print card

# def is_valid_deck(deck):
#     if ('card') != Basic:
#         if deck.count('card') > 4:
#             print "deck not valid!"
#         else:
#             print "deck valid"
#         
# print is_valid_deck(deck)