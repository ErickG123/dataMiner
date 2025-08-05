import streamlit as st

def show_visualizacao(df):
    st.subheader("🔍 Visualização Inicial dos Dados")
    st.write(df.head())
    st.subheader("📊 Estatísticas Descritivas")
    st.write(df.describe())
