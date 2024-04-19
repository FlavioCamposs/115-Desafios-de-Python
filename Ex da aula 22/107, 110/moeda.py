def aumentar(n):
    return n + (n * 20 / 100)


def diminuir(n):
    return n - (n * 10 / 100)


def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def calculo(n, p, red):
    print('=' * 25)
    print('    CALCULOS DO VALOR')
    print('=' * 25)
    print(f'{p}% de aumento: R${n+(n*p/100):.2f}')
    print(f'{p}% de redução: R${n-(n*red/100):.2f}')
    print(f'Dobro do preço:  R${n*2:.2f}')
    print(f'Metade do preço: R${n/2:.2f}')
    print('=' * 25)
