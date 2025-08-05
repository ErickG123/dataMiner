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
    if "df" not in st.session_state:
        st.session_state.df = pd.read_csv(uploaded_file)

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
        visualizacao.show_visualizacao(st.session_state.df)

    elif selected == "Tratamento de Dados":
        df_atualizado = tratamento.show_tratamento(st.session_state.df)
        if df_atualizado is not None:
            st.session_state.df = df_atualizado

        csv = st.session_state.df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📁 Baixar CSV modificado",
            data=csv,
            file_name="dados_transformados.csv",
            mime="text/csv"
        )

    elif selected == "K-Means":
        kmeans.show_kmeans(st.session_state.df)

    elif selected == "Árvore de Decisão":
        arvore_decisao.show_arvore_decisao(st.session_state.df)

    elif selected == "Regras Apriori":
        regras_apriori.show_regras_apriori(st.session_state.df)

    elif selected == "Insights Automáticos":
        insights.show_insights(st.session_state.df)

else:
    st.info("Por favor, envie um arquivo CSV para começar.")
