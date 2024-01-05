n1 = int(input('Digite um numero: '))
a = n1 - 1
d = n1 + 1
print('O numero escolhido é: {}, seu antecessor é: {}, e seu sucessor é: {}'.format(n1, a, d))

#outra forma sem criar variaveis
print('O numero escolhido é: {}, seu antecessor é: {}, e seu sucessor é: {}'.format(n1, (n1-1), (n1+1)))
