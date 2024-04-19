def numeros(*lista):
    maior = menor = 0
    print(f'Analisando os valores passados: {lista},\npercebi que o maior numero é: ', end='')
    for c in lista:
        if c == 1:
            maior = menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    print(maior)
    print('-=' * 30)


numeros(1, 3, 5, 87, 5553, 5, 687, 8, 2)
numeros(5, 22, 55, 7, 195, 14, 87, 88, 54)