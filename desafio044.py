# Elabore um programa q calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamen
# to:à vista dinheiro/cheque: 10% de desconto; à vista no cartão 5% de desconto; em até 2x no cartão preço normal; 3x
# ou mais no cartão 20% de juros.

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Qual o valor do produto: R$'))
print('''Formas de pagamento: 
[ 1 ] À vista em dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
pagamento = int(input('Qual a opção de pagamento: '))

if pagamento == 1:
    total = preco - (preco * 10) / 100
elif pagamento == 2:
    total = preco - (preco * 5) / 100
elif pagamento == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif pagamento == 4:
    total = (preco * 20) / 100 + preco
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Digite de 1 a 4.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))


