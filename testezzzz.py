from random import sample

lista = []
for numero in range(1,4):
    jogador = int(input(f'{numero}º número: '))
    lista.insert(numero, jogador)
print(lista)

jogo = list(range(1, 10))
computador = sample(jogo, 3)
print(computador)

interseccao = set(lista).intersection(computador)
print(interseccao)

quantidade = len(interseccao)
print(quantidade)

if computador == lista:
    print('Você adivinhou todos os números.')
elif quantidade == 1:
    print('acertou 1')
elif quantidade == 2:
    print('acertou 2')
else:
    print('Você não adivinhou nenhum número.')