print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Tranferidor', 4.20,
            'Compasso', 4.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

'''
FORMA NÃO MUITO VERSÁTIL:

print(f'{produtos[0]}.................R${produtos[1]}')
print(f'{produtos[2]}.................R${produtos[3]:.2f}')
print(f'{produtos[4]}.................R${produtos[5]:.2f}')
print(f'{produtos[6]}.................R${produtos[7]:.2f}')
print(f'{produtos[8]}.................R${produtos[9]:.2f}')
print(f'{produtos[10]}................R${produtos[11]:.2f}')
print(f'{produtos[12]}................R${produtos[13]:.2f}')
print(f'{produtos[14]}................R${produtos[15]:.2f}')
print(f'{produtos[16]}................R${produtos[17]:.2f}')
'''

#MELHOR FORMA
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end=' ')
    else:
        print(f'R${produtos[c]:.2f}')
print('-' * 40)