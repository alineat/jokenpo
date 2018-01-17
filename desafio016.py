# Crie um programa q leia um nº real qlquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

'''from math import trunc
num = float(input('Digite um número qualquer: '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))
'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}.'.format(num, int(num)))
