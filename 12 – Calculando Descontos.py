valor = float(input('Qual o preço do produto? '))
desconto = 0.05 #equivalente à 5% de desconto
valorDescontado = valor - (valor * desconto)
print('Parabéns, vc ganhou um desconto de 5%, o valor do produto agora ficou por R${}'.format(valorDescontado))
