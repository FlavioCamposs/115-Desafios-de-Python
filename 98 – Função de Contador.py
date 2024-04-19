def linha():
    print('-=' * 20)

def contador(inicio, fim, passo):
    linha()
    print(f'Contagem de {inicio} até {fim} em {passo}')
    for c in range(inicio, fim+1, passo):
        print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
linha()
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))