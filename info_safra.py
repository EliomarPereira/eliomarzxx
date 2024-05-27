import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt


dados = pd.read_excel("Export.xlsx")
dados.to_dict()
st.set_page_config(page_title= 'informações da safra',
                   page_icon='icons8-cana-de-açúcar-48.png')

with st.container():
    st.subheader("INFORMAÇÕES DA SAFRA 2024/2025")

    st.divider()
    
col1, col2, col3 = st.columns(3)

with st.container():
    def formatar_milhares(valor):
        return f"{valor:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")

    
    Producao_Real = dados['Produção Real (TON)'].sum()
    Producao_Estimada = dados['Produção (TON)'].sum()
    saldo = Producao_Estimada - Producao_Real


    Producao_Real_str = formatar_milhares(Producao_Real)
    Producao_Estimada_str = formatar_milhares(Producao_Estimada)
    saldo_str = formatar_milhares(saldo)

    col1.metric(label=':black[TON PREVISTAS 🏭]', value=Producao_Estimada_str, label_visibility='visible')
    col2.metric(label=':black[TON COLHIDAS 	🌿]', value=Producao_Real_str, label_visibility='visible')
    col3.metric(label=':black[SALDO]', value=saldo_str, label_visibility='visible')
    st.divider()

with st.container():
    Producao_Real = dados['Produção Real (TON)'].sum()
    Producao_Estimada = dados['Produção (TON)'].sum()
    saldo = Producao_Estimada - Producao_Real

    labels = ['PRODUÇÃO TOTAL', 'Saldo']
    sizes = [Producao_Real, saldo]

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes )])

    fig.update_layout(title="ACOMPANHAMENTO DA COLHEITA")

    st.plotly_chart(fig, use_container_width=False, sharing='streamlit', theme='streamlit')
    


with st.container():

    st.write("TON COLHIDAS POR FRENTE")

    producao = dados[dados['Produção Real (TON)'] > 0]

    comparacao = producao.groupby('FRENTE CORTE').agg({
        'Produção Real (TON)': 'sum',
        'FRENTE CORTE': 'max'
    })
    st.bar_chart(comparacao,
                 x='FRENTE CORTE',
                 y='Produção Real (TON)',
                 width=500,
                 use_container_width=False)


with st.container():

    st.write("FAZENDAS COLHIDAS")

    producao = dados[dados['Produção Real (TON)'] > 0]
    fazendas = producao.groupby('FAZENDA').agg({
        'Área Colhida (ha)': 'sum',
        'Produção Real (TON)': 'sum',
        'Produtividade (TON/ha)': 'mean'
    })

    st.dataframe(fazendas)