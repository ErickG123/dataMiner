import streamlit as st
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

def show_regras_apriori(df):
    st.subheader("🔗 Regras de Associação com Apriori")

    # Verifica se dataset está no formato binário (0 e 1)
    if set(df.dropna().stack().astype(str).str.strip().unique()).issubset({'0', '1'}):
        df_bool = df.astype(bool)
        st.success("Formato de transações válido! (valores 0 e 1)")

        min_support = st.slider("Selecione o suporte mínimo:", 0.01, 0.5, 0.1, step=0.01)
        min_confidence = st.slider("Selecione a confiança mínima:", 0.1, 1.0, 0.5, step=0.05)

        if st.button("Executar Apriori"):
            try:
                frequent_itemsets = apriori(df_bool, min_support=min_support, use_colnames=True)
                regras = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

                if not regras.empty:
                    st.session_state['regras_apriori'] = regras
                    st.success("Regras geradas com sucesso!")
                else:
                    st.warning("Nenhuma regra encontrada com os parâmetros definidos.")
            except Exception as e:
                st.error(f"Erro ao executar Apriori: {e}")

        if 'regras_apriori' in st.session_state:
            regras = st.session_state['regras_apriori'].copy()

            ordenacao = st.selectbox("Ordenar regras por:", options=["confidence", "lift"], index=0)
            regras = regras.sort_values(by=ordenacao, ascending=False)

            if st.checkbox("Mostrar apenas regras com lift > 1.2"):
                regras = regras[regras["lift"] > 1.2]

            st.write("📋 Regras encontradas:")
            regras_display = regras.copy()
            regras_display['antecedents'] = regras_display['antecedents'].apply(lambda x: ", ".join(sorted(list(x))))
            regras_display['consequents'] = regras_display['consequents'].apply(lambda x: ", ".join(sorted(list(x))))

            st.dataframe(regras_display[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

            st.subheader("🧠 Interpretação das Regras")

            def formatar_regra(row):
                antecedents = ", ".join(sorted(list(row['antecedents'])))
                consequents = ", ".join(sorted(list(row['consequents'])))
                suporte = round(row['support'] * 100, 2)
                confianca = round(row['confidence'] * 100, 2)
                lift = round(row['lift'], 2)

                if lift > 1.4:
                    cor = "🟢"
                    intensidade = "forte"
                elif lift > 1.2:
                    cor = "🟡"
                    intensidade = "moderada"
                else:
                    cor = "🔴"
                    intensidade = "fraca ou neutra"

                return (
                    f"{cor} Quando alguém compra **{antecedents}**, "
                    f"há **{confianca}% de chance** de também comprar **{consequents}**. "
                    f"O suporte é **{suporte}%**, e o lift é **{lift}** (associação {intensidade})."
                )

            explicacoes = regras.apply(formatar_regra, axis=1)
            for frase in explicacoes:
                st.markdown(f"- {frase}")
    else:
        st.warning("O dataset precisa estar no formato binário (valores 0 e 1 por item).")
