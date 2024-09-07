from random import shuffle

txt = "criptografia"
lista = list(txt)
shuffle(lista)
ale = ' - '.join(lista)
print(f'{ale}')
