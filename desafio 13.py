salarioAtual = float(input('Qual o seu salário atual? '))
aumento = 0.15
salarioAumentado = salarioAtual + (salarioAtual * aumento)
print('Parabéns, você ganhou um aumento de 15%, seu salário agora é de: R${:.3f}'.format(salarioAumentado))