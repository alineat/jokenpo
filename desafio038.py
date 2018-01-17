# Escreva um programa q leia dois nºs inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior;
# o segundo valor é maior; não existe valor maior, os dois são iguais.

n1 = int(input('Escreva um nº: '))
n2 = int(input('Escreva outro nº: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo valor é maior.')
else:
    print('Não há valor maior, os dois são iguais.')

