# Escreva um programa q converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc = float(input('Informe a temperatura em ºC: '))
tf = (tc / 5) * 9 + 32
print('A temperatura em Fahrenheit é {}ºF.'.format(tf))
