# Escreva um programa q faça o computador "pensar" em um nº inteiro entre 0 e 5 e peça p/ o usuário tentar descobrir
# qual foi o nº escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep #uso isso so p/ parecer q o computador está pensando
computador = randint(0, 5) # faz o pc pensar
jogador = int(input('Vou pensar em um nº de 0 a 5. Tente adivinhar: ')) # jogador adivinha
print('Processando...')
sleep(2)
if computador == jogador:
    print('Na mosca, você acertou!')
else:
    print('Não foi dessa vez, eu pensei no nº {}.'.format(computador))