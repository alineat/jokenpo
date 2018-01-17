import csv
def ler_dados():
    nomes = input('Digite varios nomes separados por virgula: ')
    pessoas = nomes.split(',')
    print(pessoas)
    lista = []
    for nome in pessoas:
        peso = float(input('Digite peso de {}'.format(nome)))
        altura = float(input('Digite a altura de {}'.format(nome)))
        print('Nome {} : {} kg, {}m'.format(nome, peso, altura))
        lista.append((nome, peso, altura))
    return lista
def escrever_dados(nome_arquivo, pessoas):
    colunas = ['Nome', 'Peso', 'Altura']
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas)
        writer.writeheader()
        for nome, peso, eltura in pessoas:
            pessoa = {}
            pessoa['Nome'] = nome
            pessoa['Peso'] = peso
            pessoa['Altura'] = altura
            writer.writerow(pessoa)

pessoas = ler_dados()
escrever_dados('pessoas.csv', pessoas)

