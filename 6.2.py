import random

# Oletetaan ettei noppa ole kuppanen ja tahkojen määrä = maksimisilmäluku

max = int(input('Anna maksimisilmäluku: '))

def noppa(tahkot):
    silmäluku = random.randint(1, max)
    return silmäluku

while True:
    luku = noppa(max)
    print(luku)
    if luku == max:
        break