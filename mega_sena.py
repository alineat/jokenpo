from random import sample

print('\033[31mMega-Sena\033[m\n')

jogar = 'S'
sena = quina = quadra = trena = dupla = una = zero = 0
while jogar == 'S':
    lista = []
    for numero in range(1, 61):
        a = int(numero)
        lista.insert(numero, a)
    print(lista[:10])
    print(lista[10:20])
    print(lista[20:30])
    print(lista[30:40])
    print(lista[40:50])
    print(lista[50:])

    s = input('Escolha 6 números entre 1 e 60, separe-os com vírgula: ').strip()
    numeros = list(map(int, s.split(',')))
    numeros_ordenados = sorted(numeros)
    print(numeros_ordenados)

    jogo = list(range(1, 61))
    computador = sample(jogo, 6)
    numeros_ordenados = sorted(computador)
    print(f'Números sorteados: {numeros_ordenados}')

    intersecacao = set(numeros).intersection(computador)
    acertos = len(intersecacao)

    if acertos == 6:
        print('Sena!')
        sena += 1
    elif acertos == 5:
        print('Quina!')
        quina += 1
    elif acertos == 4:
        print('Quadra!')
        quadra += 1
    elif acertos == 3:
        print('Acertou 3 números, mas não ganhou nada.')
        trena += 1
    elif acertos == 2:
        print('Acertou 2 números, mas não ganhou nada.')
        dupla += 1
    elif acertos == 1:
        print('Acertou 1 número, mas não ganhou nada.')
        una += 1
    else:
        print('Não foi dessa vez mesmo.')
        zero += 1
    jogar = str(input('Quer continuar a jogar? [s/n]')).strip().upper()[0]
else:
    print(f'''Números acertados:
Nenhum número: {zero}
Una: {una}
Dupla: {dupla}
Trena: {trena}
Quadra: {quadra}
Quina: {quina}
Sena: {sena}''')

