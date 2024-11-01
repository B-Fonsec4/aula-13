import pandas as pd 
import numpy as np 

df = pd.read_excel('vendas_roupas1.xlsx')
print(df)
categoria = df['Categoria']
quantidade_vendida = df['Quantidade Vendida']
print(quantidade_vendida)


q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)
q3 = np.quantile(quantidade_vendida, 0.75)

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print(f'Essa é a média {media}')
print(f'Essa é a mediana {mediana}')

print(quantidade_vendida.describe())
print(quantidade_vendida.unique())
# print(categoria.describe()) descreve td
# print(categoria.unique())

qtd_ven_organizada = df.sort_values(by= 'Quantidade Vendida', ascending= True)
qntd_vendida = qtd_ven_organizada['Quantidade Vendida']
print(quantidade_vendida.values)