import pandas as pd
import random

def gerar_dataset(n):
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
    return pd.DataFrame(dados, columns=colunas)

df = gerar_dataset(10000)
df.to_csv("data/clientes_varejo.csv", index=False)
print("Arquivo 'clientes_varejo.csv' gerado com sucesso!")
