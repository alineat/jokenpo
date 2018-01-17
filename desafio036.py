# programa p/ aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em qntos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo q ela não pode
# exceder 30% do salário ou então o emprétimo será negado.

casa = float(input('Qual o valor da casa que você quer comprar? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12 )
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Podemos aprovar esse empréstimo.')
else:
    print('Não podemos conceder esse empréstimo.')