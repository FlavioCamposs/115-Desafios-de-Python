valorDaCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? ')) #anos * 12, para descobrir quantos meses tem "x" anos

porcentagem = salario * 30 / 100 #tirando 30% do salário
valorPorMes = valorDaCasa / (anos * 12) #saber quanto ele vai pagar por mes durante "x" anos

if valorPorMes < porcentagem: #se a prestação mensal for menor que 30% do salário
    print('Você vai pagar R${:.2f} por mês, durante {} anos'.format(valorPorMes, anos))
else:
    print('Empréstimo negado! a prestação mensal deu R${:.2f}, ela excedeu 30% do seu salário!'.format(valorPorMes))