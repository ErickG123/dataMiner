import streamlit as st
import numpy as np

def show_insights(df):
    st.subheader("📋 Insights Automáticos")

    with st.expander("🔍 Ver insights automáticos com base no dataset"):
        insights = []

        missing = df.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            for col, qtd in missing.items():
                insights.append(f"⚠️ A coluna **{col}** possui **{qtd} valores nulos**.")
        else:
            insights.append("✅ Nenhuma coluna possui valores nulos.")

        desc = df.describe().T
        top_variancia = desc['std'].sort_values(ascending=False).head(3)
        for col, std in top_variancia.items():
            insights.append(f"📊 A coluna **{col}** apresenta alta variabilidade (desvio padrão = {std:.2f}).")

        num_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(num_cols) >= 2:
            corr = df[num_cols].corr()
            corr_pairs = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool)).stack()
            fortes = corr_pairs[abs(corr_pairs) > 0.7]
            for (col1, col2), val in fortes.items():
                insights.append(f"🔗 Correlação de **{val:.2f}** entre **{col1}** e **{col2}**.")

        if insights:
            for i in insights:
                st.markdown(f"- {i}")
        else:
            st.info("Nenhum insight relevante encontrado neste conjunto de dados.")
