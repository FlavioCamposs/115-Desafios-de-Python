def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;91mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;91mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


#LISTA DAS CORES
c = ['\033[m',          # 0 - sem cores
     '\033[1;91m',      # 1 - vermelho
     '\033[1;92m',      # 2 - verde
     '\033[1;93m',      # 3 - amarelo
     '\033[1;94m',      # 4 - azul
     '\033[1;97m',      # 5 - Branco
]


def linha(tam=42):
    return '\033[1;97m=\033[m' * tam


def cabecalho(txt, cor=0):
    print(linha())
    print(c[cor], end='')
    print(txt.center(42))
    print(c[0], end='')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL', 5)
    c = 1
    for item in lista:
        print(f'\033[1;93m{c}\033[m - \033[1;94m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;92mSua Opção: \033[m')
    return opc
