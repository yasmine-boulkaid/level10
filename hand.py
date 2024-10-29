import random

from carte import Carte
from deck import paquet_carte
from termcolor import colored
import langues


class Hand:
    def __init__(self):
        self.hand = []

    def __len__(self):
        return len(self.hand)

    def piocher_carte(self, deck):
        if len(deck) > 0:
            self.hand.append(deck[0])
            deck.pop(0)
        return self.hand

    def distribuer(self, deck):
        for i in range(1, 11):
            self.piocher_carte(deck)
        return self.hand

    def jouer_carte(self, carte):
        self.hand.remove(carte)

    def afficher_main(self, langue):
        for i in self.hand:
            i.print_carte(langue)

    def changer_cartes(self, deck, langue):
        compteur = 0
        choix = langues.remplacer(langue)
        while choix != 'y' and choix != 'n':
            choix = langues.pas_compris(langue)
        while compteur < 3 and choix == 'y':
            carte_a_tej = Carte()
            carte_voulue = langues.carte_a_tej(langue)
            carte_a_tej.to_carte(carte_voulue[0], carte_voulue[1], langue)
            if carte_a_tej in self.hand:
                self.hand.remove(carte_a_tej)
                deck.append(carte_a_tej)
                compteur += 1
                if compteur == 3:
                    pass
                else:
                    choix = langues.une_autre(langue)
                    while choix != 'y' and choix != 'n':
                        choix = langues.pas_compris(langue)
            else:
                langues.pas_dans_main(langue)
                choix = langues.remplacer(langue)
        for i in range(compteur):
            self.piocher_carte(deck)
        return self.hand

