# Crie um programa q leia uma frase qlquer e diga se ela é um palíndromo-frase q de frente para trás e de trás para fren
# te da a mesma coisa. ex apos a sopa; a sacada da casa

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1] #começa no inico ate o fim de tras para frente
#for letra in range(len(junto) - 1, -1, -1)
#    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
