import json

with open("C:/Users/mizae/OneDrive/Área de Trabalho/scripts_python/testesgithub/faturamento.json",'r') as arquivo:
    dados = json.load(arquivo)

dados_lista = [{"data":data,"valor":valor} for data, valor in dados.items()]

qtd = len(dados_lista)
soma = sum(item["valor"] for item in dados_lista)
med = soma / qtd
menor = min(item["valor"] for item in dados_lista)
maior = max(item["valor"] for item in dados_lista)

acima_med = len([item for item in dados_lista if item ["valor"] > med])

print(f'O menor valor ocorrido foi de R$ {menor:.2f}')
print(f'O maior valor ocorrido foi de R$ {maior:.2f}')
print(f'O número de dias com valor acima da média e de {acima_med}.')
