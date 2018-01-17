# Faça um programa q calcule a soma entre todos os nºs ímpares q são múltiplos de 3 e q se encontram no intervalo de 1
# até 500.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1  #ou cont += 1
        soma += c   # soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
