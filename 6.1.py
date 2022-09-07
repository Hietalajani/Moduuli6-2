import random

def noppa():
    silmäluku = random.randint(1, 6)
    return silmäluku

while True:
    luku = noppa()
    print(luku)
    if luku == 6:
        break


