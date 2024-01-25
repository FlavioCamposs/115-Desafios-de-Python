num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print('-=' * 10)
print('''O que você deseja fazer com eles?
[1] - Somar
[2] - Multiplicar
[3] - Descobrir o maior valor
[4] - Digitar novos numeros
[5] - Sair do programa''')
escolha = int(input('Escolha: '))
print('-=' * 10)

while escolha != 5:
    if escolha == 1:
        print(f'A soma entre {num1} e {num2} é: {num1 + num2}')
        escolha = int(input('Deseja fazer outra operação?: '))
    if escolha == 2:
        print(f'A multiplicação entre {num1} e {num2} é: {num1 * num2}')
        escolha = int(input('Deseja fazer outra operação?: '))
    if escolha == 3:
        print(f'O maior valor entre {num1} e {num2} é: {max(num1, num2)}')
        escolha = int(input('Deseja fazer outra operação?: '))
    if escolha == 4:
        print('Certo, digite os novos numeros!')
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        escolha = int(input('O que você deseja fazer com eles?: '))
print('Você Saiu do programa!')