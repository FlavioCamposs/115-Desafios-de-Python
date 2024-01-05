soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1 #ele vai acrescentando 1, a cada iteração do lopp
        soma += c
print('Numeros achados: {}, a soma entre eles é: {}'.format(cont, soma))
