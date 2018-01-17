# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Diga um número inteiro: '))
resultado = numero % 2
if resultado == 0:
    print('{} é par.'.format(numero))
else:
    print('{} é ímpar.'.format(numero))
#resto da divisão de qualquer n par por dois é zero, ai vc sabe se não for 0 ele é impar.