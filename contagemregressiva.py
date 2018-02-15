# Faça um progrma q mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com
# uma pausa de 1 segundo entre eles. tentar fazer donnie darko

from time import sleep
import emoji
print('Contagem regressiva!')
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print(emoji.emojize('Feliz 2018! :sparkler: :tada: :confetti_ball:', use_aliases=True))