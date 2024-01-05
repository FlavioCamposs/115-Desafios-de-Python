distancia = float(input('Qual a distancia que você irá percorrer? '))
if distancia <= 200:
    taxa = distancia * 0.50
    print('A viagem ficará por R${}'.format(taxa))
else:
    taxa = distancia * 0.45
    print('A viagem ficará por R${:.2f}'.format(taxa))
