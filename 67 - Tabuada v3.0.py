n = cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n <= 0:
        print('O valor digitado é negativo!')
        break
    print('-=' * 10)
    print(f'A tabuada de {n} é:')
    for i in range(0, 10):
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
    cont -= 10
    print('-=' * 10)