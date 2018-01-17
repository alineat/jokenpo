# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva a sua frase: ')).strip().upper()
print('A letra "A" aparece: {}.\nAparece pela primeira'
      ' vez na posição {} e pela última vez na posição {}'
      '.'.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))
