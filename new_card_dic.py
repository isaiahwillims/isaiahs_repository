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

def pull_deck_from_dic(deck):
    cards = []
    for line in deck:
        card = line.strip().split('\t')
        for i in range(int(card[1])):
            cards.append(card[0])
    return cards
    
def play_first(x):
    players = range(1, (x+1))
    play1 = random.choice(players)
    return play1
    
def draw_hand(my_deck): # line "Hand=" and "Deck =" used for trouble shooting.
    hand = my_deck[:7]
    del my_deck[:7]
    return hand, my_deck 
    
def scryx(my_deck, x):
    return my_deck[:x]

def gameplay(my_deck):
    shufle_deck(my_deck)
    handsim = draw_hand(my_deck)
    return handsim
# (do not delete) game play functions end here....

def main():

    script_name, deck1, deck2, card_info = argv
    
    basic = ['Mountain', 'Island', 'Plains', 'Forest', 'Swamp']
    legal = ['1', '2', '3', '4']
    
    file = open(card_info, 'U')
    cardname = get_card_dic(file)
    
    deck1 = open(deck1, 'U')
    deck2 = open(deck2, 'U')
    my_deck = pull_deck_from_dic(deck1)
    op_deck = pull_deck_from_dic(deck2)
    
#     x = 2
#     player_one = play_first(x)
#     print "player %s goes first" % player_one
    shufle = shufle_deck(my_deck)
    player1_hand, my_deck = draw_hand(my_deck)
    player2_habd, op_dech = draw_hand(op_deck)
    
    print player1_hand
    game_on = True
    while game_on:
        
#        card = raw_input('Play Card ')
        #put a bunch of stuff here:
        game_on = False
    
            
    play = gameplay(my_deck)
#     print gameplay(my_deck)

if __name__ == "__main__":
    main()