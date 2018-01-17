# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    preço = 0.5 * distancia
else:
    preço = 0.45 * distancia
#Dá para fazer assim:
#preço = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('O preço da passagem é R${:.2f}.'.format(preço))
