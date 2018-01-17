# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário? '))
if salario >= 1250:
    aumento = (salario * 10) / 100
else:
    aumento = (salario * 15) / 100
total = aumento + salario
print('Você receberá um aumento de R${:.2f}. '
      'Seu salário passará a ser R${:.2f}.'.format(aumento, total))