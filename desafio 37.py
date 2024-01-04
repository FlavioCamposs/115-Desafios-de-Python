print('''Faça a conversão de um número!
Digite:
[1] - Para Binário
[2] - Para Octal
[3] - Para Hexadecimal''')
num = int(input('Escreva um número: '))
escolha = int(input('Qual conversão você deseja fazer? '))
if escolha == 1:
    print('O número {} convertido para Binário é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} convertido para Octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} convertido para Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Número Inválido!')