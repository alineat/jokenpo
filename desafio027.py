# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Nome completo: ')).strip()
dividido = nome.split()
print('Primeiro nome: {}.\nSegundo nome: {}'
      '.'.format(dividido [0], dividido[len(dividido)-1]))