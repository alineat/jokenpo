# Desenvolva uma lógica q leia o peso e altura de uma pessoa, calcule seu status, de acordo com a tabela abaixo:abaixo d
# 18.5 abaixo do peso;entre 18.5 e 25 peso ideal;25 até 30 sobrepeso; 30 até 40 obesidade; acima de 40 obesidade morbida

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
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
    