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
def get_card_dictionary(file)
    for line in file:
        card_info = line.split('\t')
        if card_info[0] == 'Name': 
            cardname[card_info[1]] = {}
            cardstat = cardname[card_info[1]]
            cardstat['Name'] = card_info[1]
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


cards, values = cardname.items()

#add a card to the end of a list
cards.append(card)
#insert a card into a specific place in the deck
cards.insert(0, card)
#remove the last card form the deck and return it
cards.pop()



# 
# def is_valid_deck(deck):
#     if deck.count('some card')
#         return "deck not valid!"