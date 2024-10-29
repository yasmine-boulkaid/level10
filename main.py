import deck
import rules
from carte import Carte
from plateau import Plateau
from hand import Hand
from deck import paquet_carte
from termcolor import cprint
import langues

mon_plateau = Plateau()
ma_main = Hand()
mon_deck = deck.shuffle_deck()


def choix_langue():
    langue_voulue = input('français/english/deutsch ? ')
    while langue_voulue not in langues.liste_langue:
        print("je ne comprends pas/i don't understand/da verstehe ich nicht")
        langue_voulue = input('français/english/deutsch ? ')
    return langue_voulue


def mise_en_place(langue):
    ma_main.hand = ma_main.distribuer(mon_deck)
    mon_plateau.__init__()
    langues.regles(langue_choisie)


def tour_jeu(langue):
    ma_main.afficher_main(langue)
    mon_plateau.afficher_plateau(langue)
    carte = Carte(None, None)
    carte_a_jouer = langues.carte_voulue(langue, mon_deck)
    carte.to_carte(carte_a_jouer[0], carte_a_jouer[1], langue)
    mon_plateau.poser_carte_couleur(carte, ma_main, mon_deck, langue)
    print('deck len = ' + str(len(mon_deck)))


### MAIN ###
langue_choisie = choix_langue()
mise_en_place(langue_choisie)
compteur = 0

while len(ma_main) > 0:
    tour_jeu(langue_choisie)
    if mon_plateau.counter == 5 and rules.test_regles:
        rules.verifier_zero(mon_plateau, langue_choisie)
        rules.verifier_croissant(mon_plateau, langue_choisie)
        rules.verifier_couleurs_jouees(mon_plateau, langue_choisie)
        mon_plateau.counter = 0
print('woop woop !')

### RESTE A FAIRE ###
#   faire plein de langues (au moins anglais)
# ne pas differencier les majuscules et les minuscules psk c'est chiant
# faire en sorte de savoir combien de cartes il reste dans la pioche
        # at any time if input == pioche/deck/?? print len(deck)
# il faut pas mélanger les cartes discarded. tu les gardes dans genre discarded_deck (dans le bon ordre ie fifo) et quand len(deck) == 0 tu commences à piocher dans le discarded_deck
