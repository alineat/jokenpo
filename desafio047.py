# Crie um progrma q mostre na tela todos os nªs pares q estão no intervalo entre 1 e 50.

#for n in range(1, 51):
#    print('.', end=' ') #aqui vemos q ele faz duas iterações para poder mostrar o numeor q queremos,
#    if n % 2 == 0: #imprime o n se ele for divisivel por 2
#        print(n, end=' ')

#ou

for n in range(2, 51, 2): #pule de 2 em 2 para fazer metade das iterações e não as 50.
    print(n, end=' ')