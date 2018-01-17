n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('A sua nota é {:.1f}.'.format(media))
if media >= 6.0:
    print('Sua média foi boa, parabéns.')
else:
    print('Sua média foi baxa, estude mais.')