import numpy as np 


valor_casa = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]
media = np.mean(valor_casa)
print('Essa é a media dos valores da casa:', media)

mediana = np.median(valor_casa)
print(mediana)

print(f'O Valor mais representativo é {mediana}')
print('Os valores das casas estão muito proximos n tem muitos distantes um do outro')