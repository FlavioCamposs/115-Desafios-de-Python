valorEmReais = float(input('Quanto dinheiro você tem na carteira? '))
dolar = valorEmReais / 3.27 #de acordo com a cotação do dólar na época do vídeo
print('O valor de R${} convertido para dólar americano é de: US${:.2f}'.format(valorEmReais, dolar))
