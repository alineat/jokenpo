# Crie um programa q leia o nome de uma pessoa e diga se ela tem “Silva” no nome.

nome = str(input('Nome completo: ')).strip().upper().split()
print('Seu nome tem "Silva"? {}'.format('SILVA' in nome))


