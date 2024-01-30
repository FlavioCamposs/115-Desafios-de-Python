n = soma = cont = 0
while True:
    n = int(input('Digite um numero (Digite "999" para parar): '))
    if n == 999:
        print('Fim do programa!')
        print('-' * 10)
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} numeros e a soma deles é {soma}')