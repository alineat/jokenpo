# Faça um programa q leia um nº inteiro e diga se ele é ou não um nº primo.

num = int(input('Digite um nº: '))
tot = 0
for c in range(1, num + 1): #mais 1 pq ele cona um a menos dentro do for
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO nº {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')
