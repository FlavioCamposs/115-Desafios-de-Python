def calculo(n, p, red):
    print('=' * 25)
    print('    CALCULOS DO VALOR')
    print('=' * 25)
    print(f'{p}% de aumento: R${n+(n*p/100):.2f}')
    print(f'{p}% de redução: R${n-(n*red/100):.2f}')
    print(f'Dobro do preço:  R${n*2:.2f}')
    print(f'Metade do preço: R${n/2:.2f}')
    print('=' * 25)
