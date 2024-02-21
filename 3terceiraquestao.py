#Cálculo de métricas do faturamento mensal:

import json

# Carregando os dados do faturamento diário a partir do arquivo JSON
with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)

# Filtrando os dias com faturamento maior que zero
faturamento_diario_valido = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

# Calculando o menor valor de faturamento diário
menor_faturamento = min(faturamento_diario_valido)

# Calculando o maior valor de faturamento diário
maior_faturamento = max(faturamento_diario_valido)

# Calculando a média mensal de faturamento
media_mensal = sum(faturamento_diario_valido) / len(faturamento_diario_valido)

# Contando o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for valor in faturamento_diario_valido if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento}")
print(f"Maior valor de faturamento: R${maior_faturamento}")
print(f"Numero de dias com faturamento acima da media mensal: {dias_acima_da_media}")


# Não incluí os valores de faturamento igual a zero ao calcular o menor valor por ser mais prático porque:

# 1. Evita interpretações errôneas, já que o menor valor seria sempre zero.
# 2. Melhora a análise de tendências ao longo do tempo.
# 3. Garante uma média mais precisa do faturamento, sem distorções causadas pelos valores zero.
# 4. Permite focar nos dias de atividade real da empresa, refletindo melhor o desempenho financeiro. :D