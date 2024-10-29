import deck
import langues
import rules
from carte import Carte
from plateau import Plateau
from hand import Hand
from deck import paquet_carte
from termcolor import cprint
from termcolor import colored

from colorama import init, Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print(Fore.RED + 'Your Text' + Fore.RESET)
print('yo')

fr = 'francais'
en = 'english'
carte_test = Carte('rouge', '2')
'''carte_test.print_carte(fr)
print(type(carte_test.couleur))
langues.traduire_carte_couleur(en, carte_test)
carte_test.print_carte(en)'''

mon_plateau = Plateau()
ma_main = Hand()





