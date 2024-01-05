import math

catetoOposto = float(input('Qual o comprimento do Cateto Oposto do Triangulo? '))
catetoAdjacente = float(input('Qual o comprimento do Cateto Adjacente? '))
hipotenusa = (math.pow(catetoOposto,2)) + (math.pow(catetoAdjacente, 2))
print('Em triangulo retangulo, o seu cateto oposto é {}^2,\ne o seu cateto adjacente é {}^2,\ndepois de fazer o cálculo, descobrimos que a sua hipotenusa é: {:.2f}^2'.format(catetoOposto, catetoAdjacente, hipotenusa))
