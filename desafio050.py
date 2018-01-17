# Desenvolva um programa q leia 6 nºs inteirps e mostre a soma apenas daqueles q forem pares. Se o valor digitado for
# ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} nº(s) par(es) e a soma é {}.'.format(cont, soma))
