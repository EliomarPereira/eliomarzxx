import pandas as pd
import streamlit as st
import  plotly.express  as  px
import plotly.graph_objects as go
from teste import Infos_safra
from Plantio import infos_plantio

dados = pd.read_excel("Export.xlsx")

dados.to_dict()
st.set_page_config(page_title="TONELADAS COLHIDAS POR FRENTE",layout='wide')
st.title("TONELADAS COLHIDAS POR FRENTE")

def frentes_cortes():
    col1, col2 = st.columns(2)

    dados_geral = dados[dados['Produção Real (TON)'] >0 ]


    dados_f1 = dados_geral[dados_geral['FRENTE CORTE'] =='FRENTE-01']
    dados_f1['Diferença'] = dados_f1['Produção (TON)'] - dados_f1['Produção Real (TON)']
    frente_01 = dados_f1.groupby('FAZENDA').agg({'TON/ha': 'mean',
                                                'Produtividade (TON/ha)': 'mean',
                                                'Produção Real (TON)': 'sum',
                                                'Diferença': 'sum'
                                            })
    col1.markdown("FRENTE-01")
    col1.dataframe(frente_01)

    dados_f2 = dados_geral[dados_geral['FRENTE CORTE'] =='FRENTE-02']
    dados_f2['Diferença'] = dados_f2['Produção (TON)'] - dados_f2['Produção Real (TON)']
    frente_02 = dados_f2.groupby('FAZENDA').agg({'TON/ha': 'mean',
                                                'Produtividade (TON/ha)': 'mean',
                                                'Produção Real (TON)': 'sum',
                                                'Diferença': 'sum'
                                                })
    col1.markdown("FRENTE-02")
    col1.dataframe(frente_02)

    dados_f3 = dados_geral[dados_geral['FRENTE CORTE'] =='FRENTE-03']
    dados_f3['Diferença'] = dados_f3['Produção (TON)'] - dados_f3['Produção Real (TON)']
    frente_03 = dados_f3.groupby('FAZENDA').agg({'TON/ha': 'mean',
                                                'Produtividade (TON/ha)': 'mean',
                                                'Produção Real (TON)': 'sum',
                                                'Diferença': 'sum'
                                                })
    col2.markdown("FRENTE-03")
    col2.dataframe(frente_03)

    dados_f4 = dados_geral[dados_geral['FRENTE CORTE'] =='FRENTE-04']
    dados_f4['Diferença'] = dados_f4['Produção (TON)'] - dados_f4['Produção Real (TON)']
    frente_04 = dados_f4.groupby('FAZENDA').agg({'TON/ha': 'mean',
                                                'Produtividade (TON/ha)': 'mean',
                                                'Produção Real (TON)': 'sum',
                                                'Diferença': 'sum'
                                                })
    col2.markdown("FRENTE-04")
    col2.dataframe(frente_04)

    dados_f5 = dados_geral[dados_geral['FRENTE CORTE'] =='FRENTE-05']
    dados_f5['Diferença'] = dados_f5['Produção (TON)'] - dados_f5['Produção Real (TON)']
    frente_05 = dados_f5.groupby('FAZENDA').agg({'TON/ha': 'mean',
                                                'Produtividade (TON/ha)': 'mean',
                                                'Produção Real (TON)': 'sum',
                                                'Diferença': 'sum'
                                                })
    col1.markdown("FRENTE-05")
    col1.dataframe(frente_05)

st.sidebar.title('MENU')
options = ['Informações da Safra', 'Informações por Frente', 'Informações do Plantio']
page_selecionada = st.sidebar.radio('Escolha uma opção:', options)

if page_selecionada == 'Informações da Safra':
    Infos_safra()
elif page_selecionada == 'Informações por Frente':
    frentes_cortes()
elif page_selecionada == 'Informações do Plantio':
    infos_plantio()