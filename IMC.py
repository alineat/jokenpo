peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25: #da para usar assim 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')
