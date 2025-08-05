import pandas as pd
import random
import numpy as np

def gerar_dataset(n, prob_nulo=0.1):
    cidades = ['São Paulo', 'Rio', 'Belo Horizonte', 'Salvador', 'Curitiba']
    produtos = ['arroz', 'feijao', 'oleo', 'cafe', 'acucar']
    generos = ['M', 'F']
    comprou = ['Sim', 'Não']

    dados = []
    for i in range(n):
        idade = random.randint(18, 65)
        genero = random.choice(generos)
        renda = random.randint(1200, 8000)
        cidade = random.choice(cidades)
        produto = random.choice(produtos)
        promo = random.choices(comprou, weights=[0.6, 0.4])[0]
        visitas = random.randint(1, 10)
        gasto = visitas * random.randint(20, 100)
        dados.append([i+1, idade, genero, renda, cidade, produto, promo, visitas, gasto])

    colunas = [
        'id', 'idade', 'genero', 'renda_mensal', 'cidade',
        'produto_favorito', 'comprou_promo', 'frequencia_visitas', 'valor_total_gasto'
    ]

    df = pd.DataFrame(dados, columns=colunas)

    colunas_com_nulo = ['idade', 'genero', 'renda_mensal', 'produto_favorito']
    for col in colunas_com_nulo:
        mask = np.random.rand(n) < prob_nulo
        df.loc[mask, col] = np.nan

    return df

df = gerar_dataset(10000, prob_nulo=0.1)
df.to_csv("data/clientes_varejo.csv", index=False)
print("Arquivo 'clientes_varejo.csv' gerado com sucesso com valores nulos!")
