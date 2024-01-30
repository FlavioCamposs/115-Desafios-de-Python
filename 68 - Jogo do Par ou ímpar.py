from random import randint

v = 0
while True:
    jogador = int(input('Digite um numero: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0] #[0] pegar só a primeira letra
    print(f'Você jogou {jogador}, e o pc {pc}. Deu um total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break

    print('Vamos jogar novamente...')

print(f'GAME OVER! Você ganhou {v}x')
