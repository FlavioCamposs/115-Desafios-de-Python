nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media < 5.0:
    print('Sua média foi de {:.2f}, você está REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é de {:.2f}, você está de RECUPERAÇÃO!'.format(media))
elif media >= 7.0:
    print('Sua média é de {:.2f}, parabéns, você está APROVADO!'.format(media))
