# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? R$'))
desc = preco - (preco * 5 / 100)
print('O preço normal do produto é R${:.2f}. Com o desconto de 5% ele custa R${:.2f}.'.format(preco, desc))

