# 🧠 DataMiner

**DataMiner** é uma aplicação web interativa construída com [Streamlit](https://streamlit.io/) para **exploração, visualização e mineração de dados a partir de arquivos CSV**, sem necessidade de programação.

Ideal para estudantes, professores e analistas iniciantes, o DataMiner permite carregar dados e aplicar técnicas clássicas de análise como **K-Means**, **Árvore de Decisão** e **Regras de Associação com Apriori**, tudo de forma visual, simples e guiada. 

O projeto é modular, extensível e focado em ensino e prototipagem rápida de análises — sendo uma alternativa leve e personalizável a ferramentas mais pesadas como Orange ou Exploratory.

---

## 🔧 Funcionalidades principais

- 📁 Upload de arquivos CSV com preview e estatísticas
- 📊 Visualização de dados (estatísticas, histograma, correlação, nulos)
- 🧹 Pré-tratamento básico de colunas e valores faltantes
- 📈 Agrupamento com algoritmo **K-Means** (com visualização)
- 🌳 Classificação com **Árvore de Decisão** (e acurácia)
- 🔗 Mineração de **Regras de Associação com Apriori**
- 💡 Geração automática de **insights**
- 📚 Interface amigável com navegação lateral (sidebar)
- ✅ Estrutura de código organizada em módulos

---

## 🚀 Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/dataMiner.git
cd dataMiner

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o app
streamlit run app.py
```

📦 Requisitos
- Python 3.9+
- streamlit
- pandas
- seaborn
- scikit-learn
- matplotlib
- mlxtend
- streamlit-option-menu

📘 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.
