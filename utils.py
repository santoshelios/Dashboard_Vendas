from dataset import df
import pandas as pd
import streamlit as st
import time


def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'


# Manipulando dados para gerar os gráficos ---- Manter o DF Original
# 1 - Receita por Estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()

# Removendo valores duplicados
df_rec_estado = df.drop_duplicates(subset=('Local da compra'))[['Local da compra','lat','lon']].merge(
   df_rec_estado,
   left_on= 'Local da compra',
   right_index= True).sort_values('Preço',ascending=False)



# 2 - DataFrame - Receita Mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()

# Extraindo Datas (Intervalos) da coluna 'Data da Compra'
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()

# 3 - DataFrame - Receitas por Categoria
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço',ascending=False)

# 4 - DataFrame Vendedores
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum','count']))


# Função para conveter arquivo '.CSV'
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensgem_sucesso():
    sucess = st.success(
        'Arquivo baixado com sucesso',
        icon='✅'
    )
    time.sleep(3)
    sucess.empty()
    
