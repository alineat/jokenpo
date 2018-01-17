# Faça um programa q leia um ângulo qlquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
an = float(input('Qual o ângulo em º: '))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print('Com um ângulo de {}º, seu seno vale {:.2f}, seu cosseno vale {:.2f} e a tangente vale {:.2f}.'.format(an, se, co,
                                                                                                             ta))
