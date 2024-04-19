def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('CURSO EM VÍDEO DE PYTHON')
escreva(str(input('Digite seu nome: ')))
#escreva('Flávio Batista Campos Ferreira')