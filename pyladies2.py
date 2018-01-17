from pyladies1 import imc
nomes = input('Digite vários nomes separados por vírgula: ')
pessoas = nomes.split(',')
print(pessoas)
lista = []
for nome in pessoas:
    peso = float(input('Digite o pso de {}: '.format(nome)))
    altura = float(input('Digite o peso de {}: '.format(nome)))
    print('Nome {}: {} kg {} m.'.format(nome, peso, altura))
    lista.append(imc)