peso = float(input('Peso: '))
altura = float(input('Altura: '))
def imc(peso, altura):
    return(peso / (altura ** 2))
if imc(peso, altura) < 20:
    a = 'abaixo do peso.'
elif 20 < imc(peso, altura) <= 24.9:
    a = 'peso normal'
elif 25 < imc(peso, altura) <= 29.9:
    a = 'sobrepeso'
elif imc(peso, altura) >= 30:
    a = 'obesidade'
print('Seu IMC é {:.1f}: {}.'.format(imc(peso, altura), a))

