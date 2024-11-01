import pandas as pd
import numpy as np 


df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')
print(df)

# calculando a medida tendencia central
valor_total = df['Total']
media = np.mean(valor_total)
mediana = np.median(valor_total)
print(f'essa é a media {media}')
print(f'essa é a mediana {mediana}')
# pegando quartil
q1 = np.quantile(valor_total, 0.25)
print(f'25% das vendas estão abaixo de q1 {q1}')
q2 = np.quantile(valor_total, 0.50)
print(f'50% das vendas estão abaixo de q2 ou acima {q2}')
q3 = np.quantile(valor_total, 0.75)
print(f'75% das vendas estão acima de q3 {q1}')
# filtrando produtos com vendas superiores a 10 unidades
print('\n MEDIDAS DE TENDENCIAS CENTRAL')
print(f' Média dos preços: R$ {media:.2f}')
print(f' Mediana dos preços: R$ {mediana:.2f}')
# print(f'Q1: {q1}')
# print(f'Q2: {q2}')
# print(f'Q3: {q3}')
#pegando o produto mais vendido
mais_vendidos = df[df['Vendas (unidades)']>q3]
print(mais_vendidos)

# print(produto)
