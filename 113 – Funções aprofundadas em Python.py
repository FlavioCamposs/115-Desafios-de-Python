def leiaInt(num):
    while True:
        try:
            numeroInt = int(input(num))
        except (ValueError, TypeError):
            print('\033[1;91mERROR: por favor, digite um numero inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;91mERROR: por favor, insira um dado!\033[m')
            return 0
        else:
            return numeroInt


def leiaFloat(num):
    while True:
        try:
            numeroReal = float(input(num))
        except (ValueError, TypeError):
            print('\033[1;91mERROR: por favor, digite um numero real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;91mERROR: por favor, insira um dado!\033[m')
            return 0
        else:
            return numeroReal


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'Numero inteiro: {n1}\nNumero real: {n2}')