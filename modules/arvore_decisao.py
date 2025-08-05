import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def show_arvore_decisao(df):
    st.subheader("📋 Classificação com Árvore de Decisão")

    target = st.selectbox("Selecione a coluna alvo (variável para classificar):", df.columns)

    features = st.multiselect(
        "Selecione as colunas para usar como variáveis preditoras:",
        [col for col in df.columns if col != target and df[col].dtype in ['int64', 'float64']]
    )

    if st.button("Treinar Árvore de Decisão"):
        if len(features) == 0:
            st.warning("Selecione pelo menos uma variável preditora.")
        else:
            X = df[features]
            y = df[target]

            if y.dtype == 'object':
                y = y.astype('category').cat.codes

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            clf = DecisionTreeClassifier(random_state=42)
            clf.fit(X_train, y_train)

            y_pred = clf.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            st.write(f"Acurácia no conjunto de teste: **{acc:.2f}**")

            fig, ax = plt.subplots(figsize=(12, 8))
            plot_tree(clf, feature_names=features, class_names=[str(x) for x in clf.classes_], filled=True, ax=ax)
            st.pyplot(fig)
