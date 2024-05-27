import streamlit as st
import pandas as pd
import  plotly.express  as  px
import plotly.graph_objects as go



pl = pd.read_excel('PLANTIO DIA A DIA.xlsx', sheet_name='BD-PLANTIO DIA A DIA')
pl.to_dict()

st.set_page_config(page_title="Informações do Plantio 2024", layout='wide')
st.title("INFORMAÇÕES DO PLANTIO 2024")


pd = pl.groupby('EQUIPE') ['ÁREA PLANTADA'].sum().reset_index()
pf = pl.groupby('TIPO') ['ÁREA PLANTADA'].sum().reset_index()
def infos_plantio():
    col1, col2 = st.columns(2)

    col1.markdown("ÁREA PLANTADA POR MODALIDADE DE PLANTIO")
    col1.bar_chart(data=pf, x='TIPO', y='ÁREA PLANTADA', color="#99CC32", width=500)

    col2.markdown("ÁREA PLANTADA POR EQUIPE")
    col2.bar_chart(data=pd, x='EQUIPE', y='ÁREA PLANTADA', color="#99CC32", width=100)

    st.sidebar.title('MENU')
    options = ['Informações da Safra', 'Informações por Frente', 'Informações do Plantio']
    page_selecionada = st.sidebar.radio('Escolha uma opção:', options)

    if page_selecionada == 'Informações da Safra':
        Infos_safra()
    elif page_selecionada == 'Informações por Frente':
        frentes_cortes()
    elif page_selecionada == 'Informações do Plantio':
        infos_plantio()
    