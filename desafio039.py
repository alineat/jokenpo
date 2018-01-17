# Programa q lê o ano d nasciemnto d um jovem e informe, de acordo com sua idade: se ele ainda vai se
# alistar ao serviço militar; se é a hora de se alistar; se já passou do tempo do alistamento. Seu programa tbm deverá
# mostrar o tempo q falta ou q passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = input('Qual o seu sexo, marque F para feminino e M para masculino: ').upper().strip()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if sexo == 'F':
    print('Você é do sexo feminino e não precisa se alistar.')
elif idade == 18 and sexo == 'M':
    print('Você tem que se alistar imediatamente.')
elif idade < 18 and sexo == 'M':
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda falta {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18 and sexo == 'M': #pode colocar else q dá no msmo, mas usar elif fica mais facil de entender o programa
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
