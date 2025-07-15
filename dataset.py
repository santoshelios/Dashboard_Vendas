import json
import pandas as pd

# Carregando o arquivo
file = open('dados/vendas.json')
data = json.load(file)

# Transformando em DataFrame
df = pd.DataFrame.from_dict(data)

# Ajustando a coluna de datas
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'],format='%d/%m/%Y')

# print(df)

file.close()

