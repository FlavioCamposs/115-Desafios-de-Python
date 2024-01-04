km = int(input('Qual a velocidade do carro atual: '))
limite = 80

if km > limite:
    diferenca = km - limite
    multa = 7
    print('Você ultrapassou o limite de 80km/h, você foi multado!')
    taxa = diferenca * multa
    print('Sua multa ficará por R${}'.format(taxa))
else:
    print('Pode continuar o seu caminho!')