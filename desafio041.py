# A confederação nacinal d natação precisa d um progrma q leia o ano de nasciemnto d um atleta e mostre sua categoria
# de acordo c/ a idade:até 9 anos: mirim.até 14 anos: infantil; até 19 anos: junior; até 20 anos: sênior; acima: master.

from datetime import date
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade >= 10 and idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade >= 15 and idade <= 19:
    print('Sua categoria é JÚNIOR.')
elif idade == 20:
    print('Sua categoria é SÊNIOR.')
elif idade > 20:
    print('Sua categoria é MASTER.')
