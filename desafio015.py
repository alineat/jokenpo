# Escreva um programa q pergunte a qntdd de Km percorridos por um carro alugado e a qntdd de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km o carro percorreu? '))
dias = int(input('Quantos dias esse carro foi alugado? '))
preco = (60 * dias) + (0.15 * km)
print('O aluguel do carro custa R${:.2f}.'.format(preco))

