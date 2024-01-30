soma = quant = media = maior = menor = 0
while True:
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1

    #DESCOBRIR O MAIOR E O MENOR NUMERO, A CADA VEZ QUE UM NUMERO É COLOCADO
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    escolha = str(input('Deseja continuar? [S/N]: ')).upper()
    if escolha == 'N':
        print('O programa acabou!')
        break

media = soma / quant
print(f'Você digitou {quant} numeros, e a media entre eles é: {soma}\nO maior valor foi {maior} e o menor foi {menor}')