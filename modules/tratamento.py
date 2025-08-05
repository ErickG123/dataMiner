import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def show_tratamento(df):
    st.subheader("🧹 Tratamento de Dados")

    if st.checkbox("Mostrar valores nulos"):
        st.write(df.isnull().sum())

    cols_nulos = df.columns[df.isnull().any()].tolist()

    if cols_nulos:
        st.markdown("### Preenchimento de valores nulos")
        with st.form("form_preenchimento"):
            col_sel = st.selectbox("Escolha a coluna para preencher valores nulos:", cols_nulos)

            is_numerica = pd.api.types.is_numeric_dtype(df[col_sel])

            if is_numerica:
                metodo = st.radio("Método de preenchimento:", ("Média", "Mediana", "Moda", "Valor customizado"))
            else:
                metodo = st.radio("Método de preenchimento:", ("Moda", "Valor customizado"))

            valor_custom = None
            if metodo == "Valor customizado":
                valor_custom = st.text_input("Digite o valor para preencher:")

            submit_preenchimento = st.form_submit_button("Aplicar preenchimento")

            if submit_preenchimento:
                try:
                    if metodo == "Média":
                        valor = df[col_sel].mean()
                    elif metodo == "Mediana":
                        valor = df[col_sel].median()
                    elif metodo == "Moda":
                        valor = df[col_sel].mode().iloc[0]
                    elif metodo == "Valor customizado":
                        if is_numerica:
                            valor = float(valor_custom)
                        else:
                            valor = valor_custom
                    else:
                        st.warning("Método inválido.")
                        return df

                    df[col_sel] = df[col_sel].fillna(valor)
                    st.success(f"Coluna **{col_sel}** preenchida com `{valor}`.")
                except Exception as e:
                    st.error(f"Erro ao preencher: {e}")

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    selected_cols = st.multiselect("Selecione colunas numéricas para análise:", num_cols)

    if selected_cols:
        st.subheader("📈 Histograma das colunas selecionadas")
        for col in selected_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)

    st.markdown("### 🔄 Normalização ou Padronização")

    if num_cols.any():
        with st.form("form_escala"):
            colunas_escala = st.multiselect("Selecione colunas numéricas para escalar:", num_cols)
            tipo_escala = st.radio("Escolha o tipo de escala:", ["Normalização (0-1)", "Padronização (Z-score)"])

            submit_escala = st.form_submit_button("Aplicar escala nas colunas selecionadas")

            if submit_escala:
                try:
                    if tipo_escala == "Normalização (0-1)":
                        scaler = MinMaxScaler()
                    else:
                        scaler = StandardScaler()

                    df[colunas_escala] = scaler.fit_transform(df[colunas_escala])
                    st.success(f"Transformação '{tipo_escala}' aplicada com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao aplicar escala: {e}")

    return df
