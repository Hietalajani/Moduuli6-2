def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:
    gallonat = float(input('Anna gallonat (negatiivinen lopettaa): '))
    if gallonat < 0:
        print('Kiitos ja näkemiin!')
        break
    print(f'Litroina: {gallonat_litroiksi(gallonat)}')