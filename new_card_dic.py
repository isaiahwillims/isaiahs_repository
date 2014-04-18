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

def pull_deck_from_dic(deck, cardname):
    cards = []
    for line in deck:
        card = line.strip().split('\t')
        for i in range(int(card[1])):
            cards.append(card[0])
    return cards
    
def play_first(x, deck):
    players = range(1, (x+1))
    play1 = choice(players)
    
def draw_hand(deck):
    hand = deck[:7]
    del deck[:7]
    return hand, deck
    
def scryx(deck, x):
    return deck[:x]

def main():

    script_name, deck, card_info = argv

    basic = ['Mountain', 'Island', 'Plains', 'Forest', 'Swamp']
    legal = ['1', '2', '3', '4']
    
    file = open(card_info, 'U')
    cardname = get_card_dic(file)
    
    deck = open(deck, 'U')
    my_deck = pull_deck_from_dic(deck, cardname)
    print my_deck


if __name__ == "__main__":
    main()