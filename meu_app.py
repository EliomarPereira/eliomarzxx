import streamlit as st
import pandas as pd
import plotly.graph_objects as go



dados=pd.read_excel("Export.xlsx")
dados.to_dict()

with st.container():
    st.subheader("INFORMAÇÕES DA SAFRA 2024/2025")

col1, col2= st.columns(2)

with col1:

    st.write("TON COLHIDAS POR FRENTE")

    producao= dados[dados['Produção Real (TON)'] >0 ]
        
    comparacao= producao.groupby('FRENTE CORTE').agg({'Produção Real (TON)': 'sum',
                                                        'FRENTE CORTE': 'max'})
    st.bar_chart(comparacao, x='FRENTE CORTE', y='Produção Real (TON)', width=350, use_container_width=False)

with col2:
    Producao_Real = dados['Produção Real (TON)'].sum()
    Producao_Estimada = dados['Produção (TON)'].sum()
    saldo = Producao_Estimada - Producao_Real


    labels = ['Produção Real', 'Saldo']
    sizes = [Producao_Real, saldo]

    colors = ['#ff9999', '#66b3ff'] 
    explode = (0.1, 0)
    

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    
    fig.update_layout(title="Produção Estimada vs Produção Real")
    
    st.plotly_chart(fig)



with st.container():

    st.write("FAZENDAS COLHIDAS")

    producao= dados[dados['Produção Real (TON)']>0]
    fazendas=producao.groupby('FAZENDA').agg({'Área Colhida (ha)': 'sum',
                                              'Produção Real (TON)': 'sum',
                                              'Produtividade (TON/ha)': 'max'})

    st.dataframe(fazendas)