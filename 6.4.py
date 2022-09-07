lista = [5, 6, 29, 3]

def listan_summa(lista):
    summa = 0
    for numero in lista:
        summa += numero
    return summa

print(f'Listan summa on {listan_summa(lista)}.')