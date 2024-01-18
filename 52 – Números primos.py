num = int(input('Digite um numero: '))

#numero de divisiveis
total = 0

for c in range(1, num+1):

    #verificar se o numero é divisivel por cada numero no intervalo de 1 até o num digitadop
    if num % c == 0:
        print('\033[92m', end=' ')
        total += 1
    else:
        print('\033[91m', end=' ')
    print(f'{c}', end=' ')

#verificar se o num é dividido apenas por 2 numeros
if total == 2:
    print(f'\n\033[mO numero {num} é primo!\033[m')
else:
    print(f'\n\033[mO numero {num} não é primo!\033[m')