import streamlit as st
import pandas as pd

from modules import (
    visualizacao,
    tratamento,
    kmeans,
    arvore_decisao,
    regras_apriori,
    insights
)

st.set_page_config(page_title="DataMiner", layout="wide")
st.title("🧠 DataMiner - Visualização e Mineração de Dados CSV")

uploaded_file = st.file_uploader("📁 Envie um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    menu = st.sidebar.radio("Navegação", [
        "Visualização Inicial",
        "Tratamento de Dados",
        "K-Means",
        "Árvore de Decisão",
        "Regras Apriori",
        "Insights Automáticos"
    ])

    if menu == "Visualização Inicial":
        visualizacao.show_visualizacao(df)

    elif menu == "Tratamento de Dados":
        tratamento.show_tratamento(df)

    elif menu == "K-Means":
        kmeans.show_kmeans(df)

    elif menu == "Árvore de Decisão":
        arvore_decisao.show_arvore_decisao(df)

    elif menu == "Regras Apriori":
        regras_apriori.show_regras_apriori(df)

    elif menu == "Insights Automáticos":
        insights.show_insights(df)

else:
    st.info("Por favor, envie um arquivo CSV para começar.")
