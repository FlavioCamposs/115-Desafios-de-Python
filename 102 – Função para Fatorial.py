def fatorial(n, show=False):
    resultado = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        resultado *= c
    return resultado


num = 5
print(f'{fatorial(num, show=True)}')