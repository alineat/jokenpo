n = int(input('Escreva um número: '))
print(
    'Analisando o número {}, sabemos que: \n seu dobro é {}; \n o seu triplo é {}; \n e a sua raiz quadrada é {:.2f}.'
    .format(n, (n*2), (n*3), n**(1/2)))
