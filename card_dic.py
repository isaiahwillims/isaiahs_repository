#!/usr/bin/env python
# -*- coding: utf-8 -*-

# magic_cards = {'Witchstalker':{'Cost':'1GG', 'Type':'Creature — Wolf', 'Pow/Tgh':'(3/3)', 
#                                'Rules Text':'''Hexproof (This creature can't be the target of spells or abilities your opponents control.)
# Whenever an opponent casts a blue or black spell during your turn, put a +1/+1 counter on Witchstalker.''',
#                                 'Set/Rarity': 'Magic 2014 Core Set Rare'},
#                 'Woodborn Behemoth': } 


file = open('magic_cards.txt', 'U')
for line in file:
    name = line.split('\t')[1]
    cards[name] = card_info

# 
# cards = {}
# card_info = {}
# #Add an item to a dictionary
# # cards['key'] = 'value'
# card_info['Cost'] = '1R' 
# cards['Dragon Hatchling'] = card_info
# 
# #file = open('file_name', 'U')
# 
# def get_card_dictionary(file):
#     for line in file:
#     return card_dictionary
