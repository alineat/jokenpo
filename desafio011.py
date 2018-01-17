# Faça um programa q leia a largura e a altura de uma parede em m, calcule a sua área e a quantidade de tinta necessária
# p/ pintá-lo, sabendo que cda litro de tinta, pinta uma área de 2m^2.

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar a sua parede você precisa de {}L de tinta.'
      ''.format(larg, alt, area, tinta))


