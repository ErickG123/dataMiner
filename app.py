import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

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

    with st.sidebar:
        selected = option_menu(
            menu_title="Navegação",
            options=[
                "Visualização Inicial",
                "Tratamento de Dados",
                "K-Means",
                "Árvore de Decisão",
                "Regras Apriori",
                "Insights Automáticos"
            ],
            icons=[
                "table", "tools", "diagram-3", "tree", "link-45deg", "lightbulb"
            ],
            default_index=0
        )

    if selected == "Visualização Inicial":
        visualizacao.show_visualizacao(df)

    elif selected == "Tratamento de Dados":
        tratamento.show_tratamento(df)

    elif selected == "K-Means":
        kmeans.show_kmeans(df)

    elif selected == "Árvore de Decisão":
        arvore_decisao.show_arvore_decisao(df)

    elif selected == "Regras Apriori":
        regras_apriori.show_regras_apriori(df)

    elif selected == "Insights Automáticos":
        insights.show_insights(df)

else:
    st.info("Por favor, envie um arquivo CSV para começar.")
