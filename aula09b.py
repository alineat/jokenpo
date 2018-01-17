frase = '   Aprenda Python  '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print('{} -> eu posso perguntar quantos caracteres tem na string, mas pedindo que ele remova os espaços indesejados,'
      ' para que eles não interiram na contagem'.format(len(frase.strip())))

frase2 = 'Curso em Vídeo Python'
print(frase2[0])
#frase[0] = 'J' -> errado escrever assim

frase = frase.replace('Python', 'Android')
print(frase)
