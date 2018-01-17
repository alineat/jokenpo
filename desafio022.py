# Crie um programa q leia o nome completo de uma pessoa e mostre: nome com todas as letras maiúsculas; o nome com todas
# minúsculas; quantas letras ao todo sem considerar espaços; quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}.'.format(nome.upper()))
print('Seu nome em minúscula é {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
# para contar o comprimento do nome sem considerar os espaços entre os nomes
# vc pode subtrair os espaços, como mostrado acima. numero de caracteres - numero de espaços

#Ou
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
dividido = nome.split()
print('O seu primeiro nome tem {} letras.'.format(len(dividido[0])))

