# Crie um programa q faça o computador jogar Jokenpo com vc.

from random import randint
from time import sleep
import emoji
itens = ('Pedra','Papel', 'Tesoura')
computador = randint(0, 2)
print(emoji.emojize('''Suas opções:
[ 0 ] PEDRA :fist:
[ 1 ] PAPEL :hand:
[ 2 ] TESOURA :v:''', use_aliases=True))
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # se o pc jogar pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('Você venceu.')
    elif jogador == 2:
        print('Computador venceu.')
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0:
        print('Computador vence.')
    elif jogador == 1:
        print('EMPATE.')
    elif jogador == 2:
        print('Você venceu.')
    else:
        print('Jogada inválida.')

elif computador == 2:
    if jogador == 0:
        print('Você venceu.')
    elif jogador == 1:
        print('Computador venceu.')
    elif jogador == 2:
        print('EMPATE.')
    else:
        print('Jogada inválida.')

# print('O computador escolheu {}.'.format(itens[computador])) #itens na posição computador