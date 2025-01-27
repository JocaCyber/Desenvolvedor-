import json

# Carregar os dados de faturamento de um arquivo JSON
with open(r"C:\Users\Usuário\Nova pasta\FaturamentoDiario\faturamento.json", "r") as file:
    data = json.load(file)

# Extrair os valores de faturamento
faturamento = data["faturamento"]

# Remover os dias com faturamento zero
faturamento_validos = [valor for valor in faturamento if valor > 0]

# Calcular o menor valor de faturamento
menor_faturamento = min(faturamento_validos)

# Calcular o maior valor de faturamento
maior_faturamento = max(faturamento_validos)

# Calcular a média de faturamento (considerando apenas os dias válidos)
media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

# Contar os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
{
  "faturamento": [0, 0, 100, 200, 300, 0, 400, 0, 50, 600, 0, 0, 700, 0, 800, 0, 0, 300, 200, 100, 0, 400, 0, 0, 500, 0, 0, 900, 100, 0]
}
