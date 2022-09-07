import math

def vastine_rahalle(halkaisija, hinta):
    ala = (halkaisija/2) ** 2 * math.pi / 1000
    wörtti = hinta/ala
    return wörtti

halkaisija1 = float(input('Anna pizzan 1 halkaisija senttimetreinä: '))
hinta1 = float(input('Anna pizzan 1 hinta euroina: '))
halkaisija2 = float(input('Anna pizzan 2 halkaisija senttimetreinä: '))
hinta2 = float(input('Anna pizzan 2 hinta euroina: '))

wörtti1 = vastine_rahalle(halkaisija1, hinta1)
wörtti2 = vastine_rahalle(halkaisija2, hinta2)

if wörtti1 < wörtti2:
    print('Pizza 1 on parempi vastine rahalle.')
elif wörtti1 > wörtti2:
    print('Pizza 2 on parempi vastine rahalle.')
else:
    print('Pizzat ovat yhtä wörttejä.')


