# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = str(input('Nome da cidade: ')).strip().upper()
separe = nome.split()
print('A cidade {} começa com o nome "Santo"? {}'.format(nome, 'SANTO' == separe[0]))

#OU

#cid = str(input('Em que cidade você nasceu? ')).strip()
#print(cid[:5].upper() == 'SANTO') -> mas ele considera santos, entõ não é uma boa resposta

