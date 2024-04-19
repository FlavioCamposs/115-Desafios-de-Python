from time import sleep

#CORES
c = ('\033[m',          # 0 - sem cores
     '\033[1;97;41m',   # 1 - vermelho
     '\033[1;97;42m',   # 2 - verde
     '\033[1;97;43m',   # 3 - amarelo
     '\033[1;97;44m',   # 4 - azul
     '\033[1;97m',      # 5 - Branco em negrito
     '\033[7;97m'       # 6 - branco
)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE INTERAÇÃO PyHELP', 2)
    print(c[5], end='')
    comando = str(input('Função ou biblioteca > '))
    print(c[0], end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)