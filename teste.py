import streamlit as st
import pandas as pd
import  plotly.express  as  px
import plotly.graph_objects as go



df = pd.read_excel("Export.xlsx")

df.to_dict()

st.set_page_config(layout='wide', initial_sidebar_state='auto')

def Infos_safra(): 
    st.title("INFORMAÇÕES DA SAFRA") 
    col1, col2 = st.columns(2)
    def percentual_safra():
        prod_estimada = df['Produção (TON)'].sum()
        prod_real = df['Produção Real (TON)'].sum()
        saldo = prod_estimada - prod_real

        rotulos = ['PRODUÇÃO REAL', 'SALDO']
        valores = [prod_real, saldo]
        cores = ['', '#007FFF']

        fig = go.Figure(data=[go.Pie(labels=rotulos, values=valores, marker_colors=cores, textinfo='label+percent',)])
        fig.update_layout(title_text="ACOMPANHAMENTO DA SAFRA", title_font=dict(size=16), title_x=0.15, width=1000, height=600 )
        fig.update_traces(rotation= -0)
        return fig
    grafico_percent= percentual_safra()
    col1.plotly_chart(grafico_percent)
    col1.divider()

    def total_safra():
        prod_estimada = df['Produção (TON)'].sum()
        prod_real = df['Produção Real (TON)'].sum()
        saldo = prod_estimada - prod_real

        rotulos = ['TOTAL ESTIMADO', 'TOTAL COLHIDO']
        valores = [prod_real, saldo]
        cores = ['#99CC32', '#007FFF']

        fig = go.Figure(data=[go.Pie(labels=rotulos, values=valores, marker_colors=cores, textinfo='label+value')])
        fig.update_layout(title_text="TOTAL ESTIMADO X TOTAL COLHIDO", title_font=dict(size=16), title_x=0.15, width=1000, height=600 )
        fig.update_traces(rotation= -0)
        return fig
    grafico_total= total_safra()
    col2.plotly_chart(grafico_total)

    def toneladas_frente():
        frentes = df[df['Produção Real (TON)'] > 0]

        ton_colhidas_frente = frentes.groupby('FRENTE CORTE')['Produção Real (TON)'].sum().reset_index()
        cor = '#38B0DE'
        ton_colhidas_frente['Produção Real (TON)'] = ton_colhidas_frente['Produção Real (TON)'].round(2).apply(lambda x: f"{x:,.0f}")

        fig = go.Figure(data=[go.Bar(x=ton_colhidas_frente['FRENTE CORTE'], y=ton_colhidas_frente['Produção Real (TON)'].str.replace(',', '').astype(int), text=ton_colhidas_frente['Produção Real (TON)'],
                                    textposition='auto', marker_color=cor, width=0.6)])
        fig.update_layout(
            title_text='TON COLHIDAS POR FRENTE',
            xaxis_title='Frente de Corte',
            yaxis_title='Toneladas Colhidas',
            title_x=0.25,
            
        )
        return fig
    grafico_frente= toneladas_frente()
    col1.plotly_chart(grafico_frente)


def frentes_cortes():
    st.title("FAZENDAS COLHIDAS POR FRENTE")
    col1, col2 = st.columns(2)

    dados_geral = df[df['Produção Real (TON)'] >0 ]


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

pl = pd.read_excel('PLANTIO DIA A DIA.xlsx', sheet_name='BD-PLANTIO DIA A DIA')
pl.to_dict()


pd = pl.groupby('EQUIPE') ['ÁREA PLANTADA'].sum().reset_index()
pf = pl.groupby('TIPO') ['ÁREA PLANTADA'].sum().reset_index()
def infos_plantio():
    st.title("INFORMAÇÕES DO PLANTIO")
    col1, col2 = st.columns(2)

    col1.markdown("ÁREA PLANTADA POR MODALIDADE DE PLANTIO")
    col1.bar_chart(data=pf, x='TIPO', y='ÁREA PLANTADA', color="#99CC32", width=500)

    col2.markdown("ÁREA PLANTADA POR EQUIPE")
    col2.bar_chart(data=pd, x='EQUIPE', y='ÁREA PLANTADA', color="#99CC32")

    
st.sidebar.title('MENU')
options = ['Informações da Safra', 'Informações por Frente', 'Informações do Plantio']
page_selecionada = st.sidebar.radio('Escolha uma opção:', options)

if page_selecionada == 'Informações da Safra':
    Infos_safra()
elif page_selecionada == 'Informações por Frente':
    frentes_cortes()
elif page_selecionada == 'Informações do Plantio':
    infos_plantio()
 