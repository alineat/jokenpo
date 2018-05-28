from random import sample

print('\033[31mMega-Sena\033[m\n')
print('Escolha 6 números entre 0 e 60:')
print(f'''01 02 03 04 05 06 07 08 09 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 49 50
51 52 53 54 55 56 57 58 59 60''')  # como automatizar isso?

lista = []
for numero in range(1,7):
    jogador = int(input(f'{numero}º número: '))
    lista.insert(numero, jogador)
    #numero += 1
print(lista)

jogo = list(range(1, 61))
computador = sample(jogo, 6)
print(computador)

intersecacao = set(lista).intersection(computador)
print(intersecacao)
print(len(intersecacao))

if computador == lista:
    print('Sena!')
else:
    print('Não ganhou nada')
