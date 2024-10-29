import sys
import langues
from plateau import Plateau

test_regles = True


def verifier_zero(mon_plateau: Plateau, langue):  # il faut pas verifier après chaque carte posée
    last_rouge = mon_plateau.ligne_rouge[-1]
    last_vert = mon_plateau.ligne_vert[-1]
    last_jaune = mon_plateau.ligne_jaune[-1]
    last_magenta = mon_plateau.ligne_magenta[-1]
    last_bleu = mon_plateau.ligne_bleu[-1]  # oh avec np tu pourrais faire des dingueries

    if (last_rouge == '0' and last_vert == '0') or (last_rouge == '0' and last_jaune == '0') or (last_rouge == '0' and last_magenta == '0') or (last_rouge == '0' and last_bleu == '0') or \
       (last_vert == '0' and last_jaune == '0') or (last_vert == '0' and last_magenta == '0') or (last_vert == '0' and last_bleu == '0') or \
       (last_jaune == '0' and last_magenta == '0') or (last_jaune == '0' and last_bleu == '0') or \
       (last_magenta == '0' and last_bleu == '0'):
        sys.exit(langues.trop_0(langue))
    elif last_rouge != '0' and last_vert != '0' and last_jaune != '0' and last_magenta != '0' and last_bleu != '0':
        sys.exit(langues.aucun_0(langue))

    couleur = ['rouge', 'vert', 'jaune', 'magenta', 'bleu']
    for i in couleur:
        ligne = mon_plateau.get_ligne_voulue(i)[2:]
        if len(ligne) >= 2:
            if ligne[-1] == '0' and ligne[-2] == '0':
                sys.exit(langues.deux_0(langue))

def verifier_croissant(mon_plateau: Plateau, langue):
    lignes = [mon_plateau.ligne_rouge, mon_plateau.ligne_vert, mon_plateau.ligne_jaune, mon_plateau.ligne_magenta, mon_plateau.ligne_bleu]
    for i in lignes:
        if i[-1] == '0':
            pass
        else:
            if i[-1] < i[-2]:
                sys.exit(langues.joue_croissant(langue))

def verifier_couleurs_jouees(mon_plateau: Plateau, langue):
    len_rouge = len(mon_plateau.ligne_rouge)
    len_vert = len(mon_plateau.ligne_vert)
    len_jaune = len(mon_plateau.ligne_jaune)
    len_magenta = len(mon_plateau.ligne_magenta)
    len_bleu = len(mon_plateau.ligne_bleu)
    if len_rouge != len_vert or len_rouge != len_jaune or len_rouge != len_magenta or len_rouge != len_bleu:
        sys.exit(langues.joue_couleur(langue))
