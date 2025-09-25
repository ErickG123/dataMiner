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

🛣️ Roadmap

🔹 Versão 1.1 – Limpeza e visualização mais completa
- [X] Preenchimento de valores nulos com média/mediana/moda
- [X] Normalização e padronização (MinMax Scaler, StandardScaler)
- [ ] Heatmap de correlação
- [ ] Boxplot por variável categórica
- [ ] Detecção de outliers (Z-Score ou IQR)

🎯 Objetivo: permitir uma exploração e preparação mais profunda dos dados.

🔹 Versão 1.2 – Novos algoritmos de mineração
- [ ] Adicionar Random Forest
- [ ] Adicionar Regressão Logística
- [ ] Adicionar K-Nearest Neighbors
- [ ] Avaliação de modelos: matriz de confusão, precisão, recall, F1

🎯 Objetivo: ampliar o leque de modelos preditivos e métricas.

🔹 Versão 1.3 – Qualidade de dados e diagnósticos
- [ ] Identificação de colunas com baixa variância
- [ ] Verificação de colunas com tipos mistos
- [ ] Colunas duplicadas ou altamente correlacionadas
- [ ] Verificador automático com "sugestões" de limpeza

🎯 Objetivo: identificar problemas sutis que afetam a análise.

🔹 Versão 1.4 – Funcionalidades interativas e utilitárias
- [ ] Botão para baixar dataset processado
- [ ] Exportar regras Apriori como CSV
- [ ] Geração de relatório em PDF ou HTML (com gráficos e insights)
- [ ] Carregamento de datasets padrão (Titanic, Iris, Market Basket)

🎯 Objetivo: facilitar o uso educacional e a exportação de resultados.

🔹 Versão 2.0 – Experiência orientada a ensino
- [ ] “Modo Assistido”: passos guiados com explicações (ex: "Agora escolha um target")
- [ ] Tooltips explicativos em widgets
- [ ] Abas para comparar modelos (ex: Árvore vs. Random Forest)
- [ ] Histórico de transformações no dataset
- [ ] Interface multilíngue (ex: EN/PT)

🎯 Objetivo: transformar o DataMiner em uma ferramenta de ensino acessível e didática.

📘 Licença
Distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.
