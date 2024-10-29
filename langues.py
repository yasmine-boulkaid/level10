from termcolor import cprint
from termcolor import colored
### en cours (pas fait les bold) ###
from colorama import Fore, Back, Style
import carte

liste_langue = ['français', 'francais', 'english', 'deutsch']
rouge = ['rouge', 'red', 'rot']
vert = ['vert', 'green', 'türkis']
jaune = ['jaune', 'yellow', 'gelb']
magenta = ['magenta', 'magenta', 'magenta']
bleu = ['bleu', 'blue', 'blau']


def regles(langue):
    if langue == 'français' or langue == 'francais':
        explication = input('je vous explique les règles ? (y/n) ')
        if explication == 'y':
            print("DÉROULEMENT D'UNE MANCHE : \n"
                  "vous devez poser cinq cartes\n"
                  "le format à respecter pour poser une carte est ")
            print(Fore.YELLOW + 'XY' + Fore.RESET)
            # cprint("XY", "yellow", attrs=["bold"], end=' ')
            print(
                "avec X la première lettre de la couleur (Rouge, Vert, Jaune, Magenta, Bleu) et Y le numéro de la carte. Par exemple, m1 correspond à la carte magenta, 1\n"
                "REGLES A RESPECTER :\n"
                "1. une carte de chaque couleur doit être posée par manche\n"
                "2. les cartes de même couleur doivent être posées par ordre croissant\n"
                "3. à chaque manche vous devez ré-initialiser (ie. poser un 0)", end=' ')
            print(Fore.RED + 'exactement' + Fore.RESET)
            # cprint("exactement", "red", attrs=["bold"], end=' ')
            print(
                "une couleur. Les 0 ne se trouveront jamais dans votre main. \nIl y a deux 0 par couleurs et ils se trouvent sur le plateau en début de partie. C'est à vous de les utiliser au bon moment.\n"
                "4. vous ne pouvez pas ré-initialiser la même couleur deux manches de suite\n"
                "NB : \n"
                "quand vous jouez un 0, vous pouvez changer de 0 à 3 cartes de votre main. Les cartes que vous changez se retrouveront en bas de la pioche.\n")
        print("que le jeu commence")
    elif langue == 'english':
        explication = input('do you want me to explain the rules ? (y/n) ')
        if explication == 'y':
            print("GAME ROUND : \n"
                  "you need to play five cards\n"
                  "to play a card you need to respect the format ")
            print(Fore.YELLOW + 'XY' + Fore.RESET)
            # cprint("XY", "yellow", attrs=["bold"], end=' ')
            print(
                "with X the first letter of the color (Red, Green, Yellow, Magenta, Blue) and Y the card's number. For example, m1 represents the magenta, 1 card\n"
                "RULES :\n"
                "1. you must play one card of each color per round\n"
                "2. for each color, the cards must be put down from smallest to biggest\n"
                "3. during each round you must reset (ie. put down a 0)", end=' ')
            print(Fore.RED + 'exactly' + Fore.RESET)
            # cprint("exactly", "red", attrs=["bold"], end=' ')
            print(
                "one color. You will never have a 0 in your hand. \nThere are two 0s per color and they are on the board when the game starts. Use them wisely.\n"
                "4. you can't reset the same color two times in a row\n"
                "NB : \n"
                "when you play a 0, you get to change from 0 to 3 cards in your hand. The cards you discarded will go at the bottom of the deck\n")
        print("let the game begin")
    elif langue == 'deutsch':
        explication = input('soll ich dir die Regeln erklären ? (y/n) ')
        if explication == 'y':
            print("SPIELRUNDE : \n"
                  "du musst fünf Karten auspielen\n"
                  "um eine Karte auszuspielen, musst du dem Format folgen. ")
            print(Fore.YELLOW + 'XY' + Fore.RESET)
            # cprint("XY", "yellow", attrs=["bold"], end=' ')
            print(
                "mit X als erstem Buchtaben der Farbe (Rot, Grün, Gelb, Magenta, Blau) und Y als Nummer der Karte. zum Beispiel repräsentiert m1 die Karte Magenta der Nummer 1\n"
                "SPIELREGELN :\n"
                "1. Jede Runde musst du genau eine Karte jeder Farbe ausspielen\n"
                "2. Für jede Farbe müssen die Karten von klein nach gross ausgespielt werden\n"
                "3. Jede Runde musst du eine Farbe zurücksetzen, indem du eine Null ausspielst ", end=' ')
            print(Fore.RED + 'exakt' + Fore.RESET)
            # cprint("exakt", "red", attrs=["bold"], end=' ')
            print(
                "eine Farbe. Du wirst niemals eine Null in deiner Hand haben. \nPro Farbe gibt es zwei Nullen und sie sind vorhanden, wenn das Spiel startet. Gebrauche sie weise.\n"
                "4. Du kannt die gleiche Farbe nicht zweimal hintereinander zurücksetzen\n"
                "NB : \n"
                "Wenn du eine Null augespielt hast, kannst 0-3 Karten in deiner Hand ausstauchen. Die Karte, die du ausgetauscht hast, kommt an das Ende des Kartenstapels\n")
        print("Lasst die Spiele beginnen")


def carte_voulue(langue, deck):
    if langue == 'français' or langue == 'francais':
        carte = input("quelle carte souhaitez vous jouer ? ")
        if carte == 'pioche':
            print('il y a ' + str(len(deck)) + ' cartes dans la pioche')
        else:
            while len(carte) != 2:
                print("ceci n'est pas une carte")
                carte = input("quelle carte souhaitez vous jouer ? ")
    elif langue == 'english':
        carte = input('which card do you want to play? ')
        while len(carte) != 2:
            print("this is not a card")
            carte = input("which card do you want to play?")
    elif langue == 'deutsch':
        carte = input('welche karte willst du ausspielen? ')
        while len(carte) != 2:
            print("das ist keine karte")
            carte = input("welche karte willst du ausspielen?")
    return carte


def remplacer(langue):
    if langue == 'français' or langue == 'francais':
        choix = input('voulez vous remplacer des cartes de votre main ? (y/n) ')
    elif langue == 'english':
        choix = input('do you want to change the cards in your hand ? (y/n) ')
    elif langue == 'deutsch':
        choix = input("willst du die karten in deiner hand ausstauschen? (y/n)")
    return choix


def pas_compris(langue):
    if langue == 'français' or langue == 'francais':
        choix = input("je n'ai pas compris, voulez vous remplacer des cartes de votre main ? (y/n) ")
    elif langue == 'english':
        choix = input("i didn't understand, do you want to change the cards in your hand ? (y/n) ")
    elif langue == 'deutsch':
        choix = ("das habe ich nicht verstanden, willst du die karten in deiner hand ausstauschen? (y/n)")
    return choix


def carte_a_tej(langue):
    if langue == 'français' or langue == 'francais':
        tej = input("quelle carte veux tu tej ? ")
    elif langue == 'english':
        tej = input("which card do you want to discard? ")
    elif langue == 'deutsch':
        tej = ('welche karte willst du loswerden?')
    return tej


def une_autre(langue):
    if langue == 'français' or langue == 'francais':
        choix = input('tu veux en tej une autre ? (y/n) ')
    elif langue == 'english':
        choix = input('do you want to discard another one? (y/n) ')
    elif langue == 'deutsch':
        choix = input("willst du eine weitere karte loswerden? (y/n)")
    return choix


def pas_dans_main(langue):
    if langue == 'français' or langue == 'francais':
        print("cette carte n'est pas dans ta main")
    elif langue == 'english':
        print("this card is not in your hand")
    elif langue == 'deutsch':
        print("diese karte existiert nicht in deiner hand")


def pas_une_carte(langue):
    if langue == 'français' or langue == 'francais':
        print("ceci n'est pas une carte")
    elif langue == 'english':
        print("this is not a card")
    elif langue == 'deutsch':
        print('das ist keine karte')


def plus_de_0(langue, couleur):
    if langue == 'français' or langue == 'francais':
        print('vous ne pouvez plus jouer de 0 ' + couleur)
    elif langue == 'english':
        print("you don't have anymore " + couleur + ' zeros to play')
    elif langue == 'deutsch':
        print("du kannst keine Null der Farbe" + couleur + " mehr ausspielen")


def trop_0(langue):
    if langue == 'français' or langue == 'francais':
        return 'looser \ntrop de 0 dans la colonne'
    elif langue == 'english':
        return 'looser \ntoo many zeros in the column'
    elif langue == 'deutsch':
        return "looser \nzu viele nullen in der spalte"


def aucun_0(langue):
    if langue == 'français' or langue == 'francais':
        return 'looser \naucun 0 dans la colonne'
    elif langue == 'english':
        return 'looser \nno zeros in the column'
    elif langue == 'deutsch':
        return 'looser\nkeine nullen in der spalte '


def deux_0(langue):
    if langue == 'français' or langue == 'francais':
        return 'looser \ndeux 0 à la suite'
    elif langue == 'english':
        return 'looser \ntwo zeros in a row'
    elif langue == 'deutsch':
        return 'looser \nzwei nullen in einer reihe'


def joue_croissant(langue):
    if langue == 'français' or langue == 'francais':
        return 'looser \nà cause des nb pas croissants'
    elif langue == 'english':
        return 'looser \nnumbers are not in ascending order'
    elif langue == 'deutsch':
        return "looser \ndie nummern sind nicht in aufsteigender reihenfolge"


def joue_couleur(langue):
    if langue == 'français' or langue == 'francais':
        return 'looser \npas joué toutes les couleurs'
    elif langue == 'english':
        return "looser \nyou didn't play every color"
    elif langue == 'deutsch':
        return "looser \ndu hast nicht alle farben ausgespielt"


def pas_compris_couleur(langue):
    if langue == 'français' or langue == 'francais':
        return 'je ne comprends pas de quelle COULEUR vous voulez parler'
    elif langue == 'english':
        return "i don't understand the COLOR"
    elif langue == 'deutsch':
        return "ich verstehe die FARBE nicht"


def pas_compris_numero(langue):
    if langue == 'français' or langue == 'francais':
        return 'je ne comprends pas de quel NUMERO vous voulez parler'
    elif langue == 'english':
        return "i don't understand the NUMBER"
    elif langue == 'deutsch':
        return "ich verstehe die NUMMER nicht"


def liste_couleurs(langue):
    if langue == 'français' or langue == 'francais':
        return ['rouge', 'vert', 'jaune', 'magenta', 'bleu']
    elif langue == 'english':
        return ['red', 'green', 'yellow', 'magenta', 'blue']
    elif langue == 'deutsch':
        return ['rot', 'türkis', 'gelb', 'magenta', 'blau']


def liste_coul(langue):
    if langue == 'français' or langue == 'francais':
        return ['r', 'v', 'j', 'm', 'b']
    elif langue == 'english':
        return ['r', 'g', 'y', 'm', 'b']
    elif langue == 'deutsch':
        return ['r', 't', 'g', 'm', 'b']


def lettre_to_mot(langue, carte, coul):
    if langue == 'français' or langue == 'francais':
        if coul not in liste_coul(langue):
            pas_compris_couleur(langue)
        elif coul == 'r':
            carte.couleur = 'rouge'
        elif coul == 'v':
            carte.couleur = 'vert'
        elif coul == 'j':
            carte.couleur = 'jaune'
        elif coul == 'm':
            carte.couleur = 'magenta'
        elif coul == 'b':
            carte.couleur = 'bleu'
    elif langue == 'english':
        if coul not in liste_coul(langue):
            pas_compris_couleur(langue)
        elif coul == 'r':
            carte.couleur = 'red'
        elif coul == 'g':
            carte.couleur = 'green'
        elif coul == 'y':
            carte.couleur = 'yellow'
        elif coul == 'm':
            carte.couleur = 'magenta'
        elif coul == 'b':
            carte.couleur = 'blue'
    elif langue == 'deutsch':
        if coul not in liste_coul(langue):
            pas_compris_couleur(langue)
        elif coul == 'r':
            carte.couleur = 'rot'
        elif coul == 't':
            carte.couleur = 'türkis'
        elif coul == 'y':
            carte.couleur = 'gelb'
        elif coul == 'm':
            carte.couleur = 'magenta'
        elif coul == 'b':
            carte.couleur = 'blau'


def print_couleur_langue(langue, carte):
    if langue == 'français' or langue == 'francais':
        if carte.couleur == 'rouge':
            # print(Fore.RED + 'rouge ' + str(carte.numero) + Fore.RESET)
            print(colored('rouge ' + str(carte.numero), 'red'), end=' ')
        elif carte.couleur == 'vert':
            # print(Fore.GREEN + 'vert ' + str(carte.numero) + Fore.RESET)
            print(colored('vert ' + str(carte.numero), 'green'), end=' ')
        elif carte.couleur == 'jaune':
            # print(Fore.YELLOW + 'jaune ' + str(carte.numero) + Fore.RESET)
            print(colored('jaune ' + str(carte.numero), 'yellow'), end=' ')
        elif carte.couleur == 'magenta':
            # print(Fore.MAGENTA + 'magenta ' + str(carte.numero) + Fore.RESET)
            print(colored('magenta ' + str(carte.numero), 'magenta'), end=' ')
        else:
            # print(Fore.BLUE + 'bleu ' + str(carte.numero) + Fore.RESET)
            print(colored('bleu ' + str(carte.numero), 'blue'), end=' ')
    elif langue == 'english':
        if carte.couleur == 'red':
            print(Fore.RED + 'red ' + str(carte.numero) + Fore.RESET)
            # print(colored('red ' + str(carte.numero), 'red'), end=' ')
        elif carte.couleur == 'green':
            print(Fore.GREEN + 'green ' + str(carte.numero) + Fore.RESET)
            # print(colored('green ' + str(carte.numero), 'green'), end=' ')
        elif carte.couleur == 'yellow':
            print(Fore.YELLOW + 'yellow ' + str(carte.numero) + Fore.RESET)
            # print(colored('yellow ' + str(carte.numero), 'yellow'), end=' ')
        elif carte.couleur == 'magenta':
            print(Fore.MAGENTA + 'magenta ' + str(carte.numero) + Fore.RESET)
            # print(colored('magenta ' + str(carte.numero), 'magenta'), end=' ')
        elif carte.couleur == 'blue':
            print(Fore.BLUE + 'blue ' + str(carte.numero) + Fore.RESET)
            # print(colored('blue ' + str(carte.numero), 'blue'), end=' ')
    elif langue == 'deutsch':
        if carte.couleur == 'rot':
            print(Fore.RED + 'rot ' + str(carte.numero) + Fore.RESET)
            # print(colored('rot ' + str(carte.numero), 'red'), end=' ')
        elif carte.couleur == 'türkis':
            print(Fore.CYAN + 'türkis ' + str(carte.numero) + Fore.RESET)
            # print(colored('türkis ' + str(carte.numero), 'cyan'), end=' ')
        elif carte.couleur == 'gelb':
            print(Fore.YELLOW + 'jaune ' + str(carte.numero) + Fore.RESET)
            # print(colored('gelb ' + str(carte.numero), 'yellow'), end=' ')
        elif carte.couleur == 'magenta':
            print(Fore.MAGENTA + 'magenta ' + str(carte.numero) + Fore.RESET)
            # print(colored('magenta ' + str(carte.numero), 'magenta'), end=' ')
        elif carte.couleur == 'blau':
            print(Fore.BLUE + 'blau ' + str(carte.numero) + Fore.RESET)
            # print(colored('blau ' + str(carte.numero), 'blue'), end=' ')


def traduire_carte_couleur(langue, carte):
    if langue == 'français' or langue == 'francais':
        pass
    elif langue == 'english':
        if carte.couleur == 'rouge':
            carte.couleur = 'red'
        elif carte.couleur == 'vert':
            carte.couleur = 'green'
        elif carte.couleur == 'jaune':
            carte.couleur = 'yellow'
        elif carte.couleur == 'magenta':
            carte.couleur = 'magenta'
        elif carte.couleur == 'bleu':
            carte.couleur = 'blue'
        return carte
    elif langue == 'deutsch':
        if carte.couleur == 'rouge':
            carte.couleur = 'rot'
        elif carte.couleur == 'vert':
            carte.couleur = 'türkis'
        elif carte.couleur == 'jaune':
            carte.couleur = 'gelb'
        elif carte.couleur == 'magenta':
            carte.couleur = 'magenta'
        elif carte.couleur == 'bleu':
            carte.couleur = 'blau'
        return carte
