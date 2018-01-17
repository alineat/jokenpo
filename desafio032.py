# programa q leia o ano e mostre se ele é bissexto

from datetime import date
ano = int(input('Que ano vc quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))

# para pegar o ano atual do computador import um módulo
# ano bissexto não termina em 00 e é divisível por 4.
# exceto nºs múltiplos de 100 q não são multiplos de 400.