# Programa q leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(
    '{} m equivale a:\n{} dm;\n{} cm;\n{}mm;\n{} dam;\n{} hm;\ne {} km.'.format(medida, dm, cm, mm, dam, hm, km))

