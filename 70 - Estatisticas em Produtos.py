preco = soma = prod = menor = quant = 0
barato = ''
while True:
    produto = str(input('Qual o nome do produto?: '))
    preco = float(input('Qual o preço do produto?: '))
    soma += preco
    quant += 1

    while True:
        pc = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if pc == 'S' or pc == 'N':
            break
        else:
            print('Dado invalido! digite apenas S ou N')

    if preco > 1000:
        prod += 1

    if quant == 1 or preco < menor:
        menor = preco
        barato = produto

    if pc == 'N':
        break

print('-' * 10, 'Fim do Programa', '-' * 10)
print(f'Você comprou {quant} produtos')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {prod} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato}, que custa {menor:.2f}')