# Faça um programa que abra e reproduza o áudio de um arquivo mp3
'''
from pygame import mixer
mixer.init()
mixer.music.load('desafio021.mp3')
mixer.music.play()
input('Agora vc escuta? ')
'''

import playsound
playsound.playsound('desafio021.mp3')