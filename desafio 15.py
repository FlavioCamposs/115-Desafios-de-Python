valorDoCarro = 60 #valor fixo
valorDoKm = 0.15
dias = int(input('Por quantos dias o carro foi alugado? '))
kmRodado = float(input("Quanto km's foram rodados? "))
#carro custa R$60 por dia, e R$0.15 por km rodado
valorPorDia = valorDoCarro * dias #posso também fazer o cálculo direto, sem criar uma variável
valorPorKm = valorDoKm * kmRodado
calculo = valorPorDia + valorPorKm
print('Você irá pagar uma taxa de R${:.2f}, pelo carro'.format(calculo))