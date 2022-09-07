lista = [1, 2, 3, 4, 5, 6]
parilliset_lista = []

def parittomat_pois(lista):
    for numero in lista:
        if numero % 2 == 0:
            parilliset_lista.append(numero)
        else:
            continue

parittomat_pois(lista)
print(lista)
print(parilliset_lista)