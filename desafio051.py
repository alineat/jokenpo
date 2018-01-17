# Desenvolva um programa q leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

print('=' * 6, '10 TERMOS DE UMA PA', '=' * 6)
pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
decimo = pri + (10 - 1) * ra #formula matematica para saber qual o 10º termo
for c in range(pri, decimo + ra, ra):
    print('{}'.format(c), end=' -> ')
print('Acabou.')
