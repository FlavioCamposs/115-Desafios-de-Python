def area(l, c):
    print('-' * 30)
    print('     DIMENSÕES DO TERRENO')
    print('-' * 30)
    a = l * c
    print(f'A área do terreno {l}x{c} é de {a}m2')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (c): '))
area(largura, comprimento)