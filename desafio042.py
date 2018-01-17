# Refaça o desafio 035 dos triângulos, acrescnetando o recursos de mostar o tipo de triâncgulo q será formado:
# equilátero todos os lados iguais; isósceles dois lados iguais; escaleno todos os lados diferentes.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segment: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
