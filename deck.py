from carte import Carte
import random

paquet_carte = [Carte("rouge", '1'), Carte("rouge", '2'), Carte("rouge", '3'), Carte("rouge", '4'), Carte("rouge", '5'), Carte("rouge", '6'), Carte("rouge", '7'), Carte("rouge", '8'),
                Carte("vert", '1'), Carte("vert", '2'), Carte("vert", '3'), Carte("vert", '4'), Carte("vert", '5'), Carte("vert", '6'), Carte("vert", '7'), Carte("vert", '8'),
                Carte("jaune", '1'), Carte("jaune", '2'), Carte("jaune", '3'), Carte("jaune", '4'), Carte("jaune", '5'), Carte("jaune", '6'), Carte("jaune", '7'), Carte("jaune", '8'),
                Carte("magenta", '1'), Carte("magenta", '2'), Carte("magenta", '3'), Carte("magenta", '4'), Carte("magenta", '5'), Carte("magenta", '6'), Carte("magenta", '7'), Carte("magenta", '8'),
                Carte("bleu", '1'), Carte("bleu", '2'), Carte("bleu", '3'), Carte("bleu", '4'), Carte("bleu", '5'), Carte("bleu", '6'), Carte("bleu", '7'), Carte("bleu", '8')]


'''paquet_carte = [Carte("rouge", '1'), Carte("rouge", '2'), Carte("rouge", '3'),
                Carte("vert", '1'), Carte("vert", '2'), Carte("vert", '3'),
                Carte("jaune", '1'), Carte("jaune", '2'), Carte("jaune", '3'),
                Carte("magenta", '1'), Carte("magenta", '2'), Carte("magenta", '3'),
                Carte("bleu", '1'), Carte("bleu", '2'), Carte("bleu", '3')]'''

deck_len = len(paquet_carte)

def shuffle_deck():
    return random.sample(paquet_carte, deck_len)





