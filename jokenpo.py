from random import randint
from time import sleep
import emoji

jogar = 'S'
jogador_vence = comp_vence = empate = 0

while jogar == 'S':
    pedra = emoji.emojize('Pedra :fist:', use_aliases=True)
    papel = emoji.emojize('Papel :hand:', use_aliases=True)
    tesoura = emoji.emojize('Tesoura :v:', use_aliases=True)
    opcoes = (pedra, papel, tesoura)
    computador = randint(0, 2)
    print(emoji.emojize('''\033[31m------JOKENPÔ------\033[m
Escolha sua jogada:
[ 0 ] PEDRA :fist:
[ 1 ] PAPEL :hand:
[ 2 ] TESOURA :v:''', use_aliases=True))
    jogador = ''
    lista = [0, 1, 2]
    while jogador not in lista:
        jogador = int(input('Qual é a sua jogada? '))
    print('\033[31mJO\033[m')
    sleep(.3)
    print('\033[31mKEN\033[m')
    sleep(.3)
    print('\033[31mPÔ!\033[m')
    print('-=' * 11)
    print(f'Computador jogou {opcoes[computador]}.')
    print(f'Jogador jogou {opcoes[jogador]}.')

    if computador == 0:
        if jogador == 0:
            empate += 1
        elif jogador == 1:
            jogador_vence += 1
        elif jogador == 2:
            comp_vence += 1
        print('-=' * 11)

    elif computador == 1:
        if jogador == 0:
            comp_vence += 1
        elif jogador == 1:
            empate += 1
        elif jogador == 2:
            jogador_vence += 1
        print('-=' * 11)

    elif computador == 2:
        if jogador == 0:
            jogador_vence += 1
        elif jogador == 1:
            comp_vence += 1
        elif jogador == 2:
            empate += 1
        print('-=' * 11)

    print(f'''\033[31mPONTUAÇÃO\033[m
Você: {jogador_vence}
Computador: {comp_vence}''')
    jogar = str(input('Deseja continuar a jogar? '
                      '[S/N] ')).upper().strip()[0]

else:
    if jogador_vence > comp_vence:
        print(f'Você venceu o computador por {jogador_vence} a {comp_vence}.')
    elif jogador_vence < comp_vence:
        print(f'O computador venceu você por {comp_vence} a {jogador_vence}.')
    else:
        if empate > 1:
            print(f'Você e o computador empataram {empate} vezes.')
        elif empate == 1:
            print(f'Você e o computador empataram {empate} vez.')
