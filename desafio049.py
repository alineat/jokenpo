# Refaça o desafio 009, mostrando a tabuada de um número q o usuuário escolher, só q agora utilizando um laço for.

print('-*' * 7, 'TABUADA', '-*' * 7)
n = int(input('Digite o nº da tabuada que você quer: '))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(n, c, n*c))
