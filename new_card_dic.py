#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from sys import argv

def get_card_dic(file):
    cardname = {}
    cardstat = {}
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
    return cardname
    
def validate_deck(deck, basic, legal):
    for line in deck:
        card = line.strip().split('\t')
        if card[0] in basic:
            continue
        if card[1] not in legal:
            return "!!!Deck not valid!!!"
            exit
    return "Deck valid! :)"
    
# (do not delete) game play functions begin here

def shufle_deck(my_deck):
    my_deck = random.shuffle(my_deck)
    return my_deck

def pull_deck_from_dic(deck, cardname):
    cards = []
    for line in deck:
        card = line.strip().split('\t')
        for i in range(int(card[1])):
            cards.append(card[0])
    return cards
    
def play_first(x, my_deck):
    players = range(1, (x+1))
    play1 = choice(players)
    
def draw_hand(my_deck): # line "Hand=" and "Deck =" used for trouble shooting.
    line = "*" * 25
    hand = my_deck[:7]
    del my_deck[:7]
    return "Hand=", hand, line, "Deck=", my_deck 
    
def scryx(my_deck, x):
    return my_deck[:x]

def gameplay(my_deck):
    shufle_deck(my_deck)
    handsim = draw_hand(my_deck)
    return handsim
# (do not delete) game play functions end here....

def main():

    script_name, deck, card_info = argv
    
    basic = ['Mountain', 'Island', 'Plains', 'Forest', 'Swamp']
    legal = ['1', '2', '3', '4']
    
    file = open(card_info, 'U')
    cardname = get_card_dic(file)
    
    deck = open(deck, 'U')
    my_deck = pull_deck_from_dic(deck, cardname)
    
    shufle = shufle_deck(my_deck)
    handsim = draw_hand(my_deck)    
    play = gameplay(my_deck)
    print gameplay(my_deck)

if __name__ == "__main__":
    main()