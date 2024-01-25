num = cont = soma = 0
num = int(input('Digite um numero: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero: '))
print(f'fim!, você digitou {cont} numeros, e a soma entre eles é: {soma}')