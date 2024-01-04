r1 = float(input('Digite comprimento da primeira reta: '))
r2 = float(input('Digite comprimento da segunda reta: '))
r3 = float(input('Digite comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('As três retas PODEM formar um triangulo EQUILÁTERO!') #TODOS OS LADOS IGUAIS
    elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3:
        print('As três retas PODEM formar um triangulo ISÓSCELES!') #DOIS LADOS IGUAIS
    elif r1 != r2 != r3 != r1:
        print('As três retas PODEM formar um triangulo ESCALENO!') #TODOS OS LADOS DIFERENTES
else:
    print('As três retas NÃO PODEM formar um triangulo!')