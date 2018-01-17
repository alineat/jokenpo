# Faça um algoritmo q leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o seu salário? R$'))
aumento = salario + (salario * 15 / 100)
print('Seu salário atual é R${:.2f}.\nCom um aumento de 15%, você passará a ganhar R${:.2f}.'.format(salario, aumento))
