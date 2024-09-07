n = int(34)

t1 = 0
t2 = 1

if n == t1 or n == t2:
    print(f'o número {n} pertence a sequência de fibonacci.')
else:
    pertence = False
    while t2 <= n:
        t3 = t1 + t2
        if t3 == n:
            pertence = True
            break
        t1 = t2
        t2 = t3
    if pertence or n == t2:
        print(f'O número {n} pertence a sequência de fibonacci.')
    else:
        print(f'O número {n} não pertence a sequência de fibonacci.')    