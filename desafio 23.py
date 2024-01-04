numero = int(input('Digite um numero de 0 a 9999: '))
print('Analisando o numero: {}'.format(numero))
u = numero // 1 % 10 #para descobrir a unidade: pego o numero, faço a divisão inteira por 1, divido por 10 e pego o resto da divisão, esse resto é a unidade
d = numero // 10 % 10 #para descobrir a dezena
c = numero // 100 % 10 #para descobrir a centena
m = numero // 1000 % 10 #para descobrir o milhar
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))