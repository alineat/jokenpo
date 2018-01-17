frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print('Essa string possui {} caracteres.'.format(len(frase)))
print('A letra "o" aparece {} vezes.'.format(frase.count('o')))
print('Colocando nossos caracteres em upper, posso contar qntos "O" têm. Há {} "O". veja que podemos fazer combinações'
      ''.format(frase.upper().count('O')))
print('Entre o caracter 0 e o caracter 13 há {} "o".'.format(frase.count('o', 0, 13)))
print('"deo" inicia-se na posição {}.'.format(frase.find('deo')))
print('"android" está na posição {}, ou seja, não foi encontrada.'.format(frase.find('Android')))
print('Existe a palavra "Curso" na variável frase? {}'.format('Curso' in frase))
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print('{} -> está em capitalize.'.format(frase.capitalize()))
print('{} -> está em title.'.format(frase.title()))

separe = frase.split()
print('{} -> isso esta em split().'.format(separe))

dividido = frase.split()
print('Pegue a posição 2 desse dividido e quero saber qual a letra 3: {}'.format(dividido [2][3]))

print('{} -> usando o join.'.format('-'.join(separe)))

print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programer in any programing language
(whatever it may be) can pick up Python very quickly. -> uso isso para imprimir mais fácil usar três aspas""")




