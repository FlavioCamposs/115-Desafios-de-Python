def leiaInt(num):
    return f'O numero é {num}'

while True:
    numero = input('Digite um número: ')
    if numero.isnumeric():
        print(leiaInt(numero))
        break
    else:
        print('ERROR!')