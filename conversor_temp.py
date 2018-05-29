print('-'*10, 'Conversor de Temperatura', '-'*10)
print('\nConverta as medidas das principais temperaturas automaticamente:'
      '\nCelsius (ºC), Fahrenheit (ºF) e Kelvin (K).\n')

unidade = conversao = ' '
while unidade and conversao not in 'ckf':
    medida = float(input('Digite o número a ser convertido: '))
    unidade = str(input('Digite a unidade de medida da temperatura a ser convertida '
                        '[\033[31mC\033[m/\033[31mF\033[m/\033[31mK\033[m]: ')).strip().lower()
    conversao = str(input('Digite a unidade de medida para a qual você quer '
                          'converter a temperatura [C/F/K]: ')).strip().lower()

    if unidade == 'c' and conversao == 'k':
        temp = medida + 273
        print(f'{temp:.2f} K')
    elif unidade == 'c' and conversao == 'f':
        temp = (1.8*medida) + 32
        print(f'{temp:.2f} ºF')
    elif unidade == 'k' and conversao == 'c':
        temp = medida - 273
        print(f'{temp:.2f} ºC')
    elif unidade == 'k' and conversao == 'f':
        temp = 1.8 * (medida-273) + 32
        print(f'{temp:.2f} ºF')
    elif unidade == 'f' and conversao == 'c':
        temp = (medida-32) / 1.8
        print(f'{temp:.2f} ºC')
    elif unidade == 'f' and conversao == 'k':
        temp = (medida+459.67) * 5/9
        print(f'{temp:.2f} K')
    else:
        print('Opção inválida. Digite corretamente nos campos.')
