# Crie um programa q leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:media abaixo de 5: reprovado; média entre 5 e 6.9: recuperação; média 7 ou mais: aprovado.

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))
if media >= 5 and media < 7: #Ou escreve if 7 > media >= 5:
    print('RECURPERAÇÃO.')
elif media < 5:
    print('REPROVADO.')
elif media >= 7:
    print('APROVADO')
