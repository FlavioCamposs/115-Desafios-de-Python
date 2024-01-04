salario = float(input('Qual o seu salário atual: '))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
    print('Você recebeu um aumento de 10%, seu salário agora é de R${}'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Você recebeu um aumento de 15%, seu salário agora é de R${}'.format(aumento))