# Escreva um programa q leia um nº inteiro qlquer e peça p/ o usuário escolher qual será a base de conversão: 1
# para binário, 2 para octal, 3 para hexadeciomal.

num = int(input('Digite um nº inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter p/ binário
[ 2 ] Converter p/ octal
[ 3 ] Converter p/ hexadecimal''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido p/ binário é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido p/ octal é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido p/ hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')

