num = int(input('Digite um numero para descobrir o seu fatorial: '))
cont = num
fat = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')
print(f'O {num}! é: {fat}')