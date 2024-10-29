import hand
from hand import Hand
from termcolor import colored
import langues
import rules

### en cours ###
from colorama import Fore, Back, Style


class Plateau:
    def __init__(self):
        self.ligne_rouge = ['0', '0']
        self.ligne_vert = ['0', '0']
        self.ligne_jaune = ['0', '0']
        self.ligne_magenta = ['0', '0']
        self.ligne_bleu = ['0', '0']
        self.counter = 0

    def afficher_plateau(self, langue):
        print('\n')
        if langue == 'français' or langue == 'francais':
            '''print(Fore.RED + ' ROUGE    ' + str(self.ligne_rouge) + '\n', 'red' +
                  Fore.GREEN + 'VERT     ' + str(self.ligne_vert) + '\n', 'green' +
                  Fore.YELLOW + 'JAUNE    ' + str(self.ligne_jaune) + '\n', 'yellow' +
                  Fore.MAGENTA + 'MAGENTA  ' + str(self.ligne_magenta) + '\n', 'magenta' +
                  Fore.BLUE + ('BLEU     ' + str(self.ligne_bleu), 'blue'))'''

            print(colored(' ROUGE    ' + str(self.ligne_rouge) + '\n', 'red'),
                  colored('VERT     ' + str(self.ligne_vert) + '\n', 'green'),
                  colored('JAUNE    ' + str(self.ligne_jaune) + '\n', 'yellow'),
                  colored('MAGENTA  ' + str(self.ligne_magenta) + '\n', 'magenta'),
                  colored('BLEU     ' + str(self.ligne_bleu), 'blue'))
        elif langue == 'english':
            print(colored(' RED       ' + str(self.ligne_rouge) + '\n', 'red'),
                  colored('GREEN     ' + str(self.ligne_vert) + '\n', 'green'),
                  colored('YELLOW    ' + str(self.ligne_jaune) + '\n', 'yellow'),
                  colored('MAGENTA   ' + str(self.ligne_magenta) + '\n', 'magenta'),
                  colored('BLUE      ' + str(self.ligne_bleu), 'blue'))
        elif langue == 'deutsch':
            print(colored(' ROT        ' + str(self.ligne_rouge) + '\n', 'red'),
                  colored('TÜRKIS     ' + str(self.ligne_vert) + '\n', 'cyan'),
                  colored('GELB       ' + str(self.ligne_jaune) + '\n', 'yellow'),
                  colored('MAGENTA    ' + str(self.ligne_magenta) + '\n', 'magenta'),
                  colored('BLAU       ' + str(self.ligne_bleu), 'blue'))

    def get_ligne_voulue(self, couleur):
        if couleur in langues.rouge:
            return self.ligne_rouge
        elif couleur in langues.vert:
            return self.ligne_vert
        elif couleur in langues.jaune:
            return self.ligne_jaune
        elif couleur in langues.magenta:
            return self.ligne_magenta
        elif couleur in langues.bleu:
            return self.ligne_bleu

    def set_couleur_fin(self, couleur, ligne_couleur):
        if couleur in langues.rouge:
            self.ligne_rouge = ligne_couleur
        elif couleur in langues.vert:
            self.ligne_vert = ligne_couleur
        elif couleur in langues.jaune:
            self.ligne_jaune = ligne_couleur
        elif couleur in langues.magenta:
            self.ligne_magenta = ligne_couleur
        elif couleur in langues.bleu:
            self.ligne_bleu = ligne_couleur

    def set_couleur_debut(self, couleur, ligne_couleur):
        if couleur == 'rouge':
            ligne_couleur = self.ligne_rouge
        elif couleur == 'vert':
            ligne_couleur = self.ligne_vert
        elif couleur == 'jaune':
            ligne_couleur = self.ligne_jaune
        elif couleur == 'magenta':
            ligne_couleur = self.ligne_magenta
        elif couleur == 'blue':
            ligne_couleur = self.ligne_bleu
        else:
            print('là')
        # cette fonction retourne rien, elle sert à rien ???

    def poser_carte_couleur(self, carte, hand, deck, langue):
        couleur = carte.couleur
        ligne = self.get_ligne_voulue(couleur)
        if not carte.is_carte(langue) and carte != 'pioche':
            langues.pas_une_carte(langue)
            print('dans Plateau')
        else:
            nine_count = ligne.count('X')
            if carte.numero == '0':
                if nine_count == 0:
                    ligne += ['0']
                    ligne[0] = 'X'
                    hand.changer_cartes(deck, langue)
                    self.counter += 1
                elif nine_count == 1:
                    ligne += ['0']
                    ligne[1] = 'X'
                    hand.changer_cartes(deck, langue)
                    self.counter += 1
                else:
                    langues.plus_de_0(langue, couleur)
            else:
                if carte in hand.hand:
                    ligne += [carte.numero]
                    hand.jouer_carte(carte)
                    hand.piocher_carte(deck)
                    self.counter += 1
                else:
                    langues.pas_dans_main(langue)
        self.set_couleur_fin(couleur, ligne)


''' def poser_carte(self, carte, hand):
        #nine_count = ligne_x where x=[rouge, vert, jaune, violet, bleu]
        nine_count = 0
        if carte[0] == "rouge":
            if carte[1] == 0:
                if nine_count == 0:
                    self.ligne_rouge += [0]
                    self.ligne_rouge[0] = 9
                    nine_count += 1
                    print(nine_count)
                elif nine_count == 1:
                    self.ligne_rouge += [0]
                    self.ligne_rouge[1] = 9
                    nine_count += 1
                    print(nine_count)
                else:
                    print('vous ne pouvez plus jouer de 0 rouge')
            else:
                self.ligne_rouge += [carte[1]]
                hand.jouer_carte(carte)
                hand.piocher_carte()
        elif carte[0] == "vert":
            if carte[1] == 0:
                self.ligne_vert += [0]
                self.ligne_vert[0] = 9
            else:
                self.ligne_vert += [carte[1]]
                hand.jouer_carte(carte)
                hand.piocher_carte()
        elif carte[0] == "jaune":
            if carte[1] == 0:
                self.ligne_jaune += [0]
                self.ligne_jaune[0] = 9
            else:
                self.ligne_jaune += [carte[1]]
                hand.jouer_carte(carte)
                hand.piocher_carte()
        elif carte[0] == "violet":
            if carte[1] == 0:
                self.ligne_violet += [0]
                self.ligne_violet[0] = 9
            else:
                self.ligne_violet += [carte[1]]
                hand.jouer_carte(carte)
                hand.piocher_carte()
        else:
            if carte[1] == 0:
                self.ligne_bleu += [0]
                self.ligne_bleu[0] = 9
            else:
                self.ligne_bleu += [carte[1]]
                hand.jouer_carte(carte)
                hand.piocher_carte()'''
