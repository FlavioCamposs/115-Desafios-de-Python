import math

angulo = int(input('Qual o ângulo da circunferencia? '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('Aqui está as informações do ângulo de {}°:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo, seno, cosseno, tangente))