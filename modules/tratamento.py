import streamlit as st

def show_tratamento(df):
    st.subheader("🧹 Tratamento de Dados")
    if st.checkbox("Mostrar valores nulos"):
        st.write(df.isnull().sum())

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    selected_cols = st.multiselect("Selecione colunas numéricas para análise:", num_cols)

    if selected_cols:
        st.subheader("📈 Histograma das colunas selecionadas")
        import seaborn as sns
        import matplotlib.pyplot as plt
        for col in selected_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)
