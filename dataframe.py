import pandas as pd

# Seu dicionário
dados = {
    "Nome": ["João", "Maria", "Carlos"],
    "Idade": [25, 30, 22],
    "Cidade": ["Exemplo", "OutraCidade", "MaisUmaCidade"]
}

# Criar um DataFrame a partir do dicionário
df = pd.DataFrame(dados)
df.insert(column="Estado", value=None,loc=3)
df.loc[len(df)] = ["Ruben Ching", 50, "Uberlandia", "Minas Gerais"]

# Exibir o DataFrame
print(df)
