import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def show_kmeans(df):
    st.subheader("Agrupamento com K-Means")

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns

    if len(num_cols) >= 2:
        col_x = st.selectbox("Selecione a primeira variável (eixo X):", num_cols, key="x")
        col_y = st.selectbox("Selecione a segunda variável (eixo Y):", num_cols, key="y")
        k = st.slider("Escolha o número de clusters (K):", 2, 10, value=3)

        if st.button("Aplicar K-Means"):
            try:
                dados_cluster = df[[col_x, col_y]].dropna()
                modelo = KMeans(n_clusters=k, random_state=42)
                df['cluster'] = modelo.fit_predict(dados_cluster)

                fig, ax = plt.subplots()
                sns.scatterplot(data=df, x=col_x, y=col_y, hue='cluster', palette='Set2', ax=ax)
                plt.title("Visualização dos Clusters")
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Erro ao aplicar K-Means: {e}")
    else:
        st.info("Para usar K-Means, é necessário pelo menos duas colunas numéricas.")
