# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 


fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

vt = [{"estado":estado, "faturamento":faturamento} for estado, faturamento in fat.items()]

total = sum(fat.values())

percent = {estado:(valor / total)*100 for estado, valor in fat.items()}

for estado, percentual in percent.items():
    print(f'{estado}: {percentual:.2f}%')

