from termcolor import colored
import langues


class Carte:
    def __init__(self, couleur=None, numero=None):
        self.couleur = couleur  # 'rouge', 'vert', 'jaune', 'magenta', 'bleu'
        self.numero = numero    # '0', '1', '2', '3', '4', '5', '6', '7', '8'

    def to_str(self, langue):
        return self.couleur + ' ' + str(self.numero)

    def __eq__(self, other):
        if self.couleur == other.couleur and self.numero == other.numero:
            return True

    def print_carte(self, langue):
        if not self.is_carte(langue):
            print('dans Carte')
            langues.pas_une_carte(langue)
        else:
            langues.print_couleur_langue(langue, self)

    def to_carte(self, coul, num, langue):
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        langues.lettre_to_mot(langue, self, coul)
        if num not in numeros:
            langues.pas_compris_numero(langue)
        else:
            self.numero = num
        return self

    def is_carte(self, langue):
        langues.traduire_carte_couleur(langue, self)
        liste_couleurs = langues.liste_couleurs(langue)
        liste_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.couleur not in liste_couleurs:
            return False
        elif self.numero not in liste_numeros:
            return False
        else:
            return True
