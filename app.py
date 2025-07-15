import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado,grafico_rec_categoria,grafico_rec_vendedores,grafico_vendas_vendedores


# Configurando o Layout
st.set_page_config(layout='wide')

# Importanto o dataframe
from dataset import df

#Título
st.title('Dashboard de Vendas: \U0001F6D2')

# Adicionado Filtros Interativos
# Filtro por Vendedor
selecao_vendedor = st.sidebar.title('Selecione o Vendedor')
filtro_vendedor = st.sidebar.multiselect(
  'Vendedores',
  df['Vendedor'].unique()
)
# Validando o Filtro
if filtro_vendedor:
  df=df[df['Vendedor'].isin(filtro_vendedor)]

# selecao_local = st.sidebar.title('Local da Compra')
# filtro_local_compra = st.sidebar.multiselect(
#   'Local da compra',
#   df['Local da compra'].unique()
# )
# if filtro_local_compra:
#   df=df[df['Local da compra'].isin(filtro_local_compra)]


# Criando as abas
aba1, aba2, aba3 = st.tabs(['Dataset','Receita','Vendedores'])

# Trazendo o dataframe para a 'ABA1'
with aba1:
  st.dataframe(df)

# Criando as Métricas - Valores # Insights (Storytelling)  
with aba2:
  coluna1,coluna2 = st.columns(2)
  with coluna1:
    st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
    st.plotly_chart(grafico_map_estado,use_container_width=True)
    st.plotly_chart(grafico_rec_estado,use_container_width=True)
    
  with coluna2:
    st.metric('Quantidade de Vendas',format_number(df.shape[0]))
    st.plotly_chart(grafico_rec_mensal,use_container_width=True)
    st.plotly_chart(grafico_rec_categoria,use_container_width=True)
    
with aba3:
  coluna1,coluna2 = st.columns(2)
  with coluna1:
    st.plotly_chart(grafico_rec_vendedores)
  with coluna2:
    st.plotly_chart(grafico_vendas_vendedores,use_container_width=True)
    
    





