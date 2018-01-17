# Faça um programa q leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

'''co = float(input('Qual o comprimenro do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = (co**2 + ca**2) ** (1/2)
print('O cateto oposto é {}, o cateto adjacente é {} e a hipotenusa é {:.2f}.'.format(co, ca, hi))
'''

from math import hypot
co = float(input('Qual o comprimenro do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}.'.format(hi))

