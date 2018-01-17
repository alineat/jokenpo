# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Isso é usado para testar se ele pode ser convertido lá na frente do tipo primitivo, para número etc.
x = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(x)))
print('É um número? {} '.format(x.isnumeric()))
print('É alfabético? {}'.format(x.isalpha()))
print('Só tem espaços? {}'.format(x.isspace()))
print('É alfanumérico? {}'.format(x.isalnum()))
print('Está em maiúscula? {}'.format(x.isupper()))
print('Está em minúscula? {}'.format(x.islower()))
print('Está capitalizada? {}'.format(x.istitle()))
print('Ela pode ser um identificador? {}'.format(x.isidentifier()))

