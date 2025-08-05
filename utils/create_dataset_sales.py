import pandas as pd
import random

def gerar_dataset_transacoes(n=1000):
    produtos = ['arroz', 'feijao', 'oleo', 'cafe', 'acucar', 'leite', 'macarrao']
    dados = []

    for _ in range(n):
        transacao = {}
        for produto in produtos:
            # Simula chance de compra entre 10% e 60%
            transacao[produto] = 1 if random.random() < random.uniform(0.1, 0.6) else 0
        dados.append(transacao)

    df_transacoes = pd.DataFrame(dados)
    return df_transacoes

# Gerar e salvar o dataset
df_apriori = gerar_dataset_transacoes(1000)
df_apriori.to_csv("data/transacoes_produtos.csv", index=False)
print("Arquivo 'transacoes_produtos.csv' gerado com sucesso!")
