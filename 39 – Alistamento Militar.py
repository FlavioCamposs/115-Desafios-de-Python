import datetime

ano = int(input('Qual o ano do seu nascimento? '))

anoAtual = datetime.datetime.now().year #pegando o ano atual do sistema
id = anoAtual - ano

if id < 18:
    anos = 18 - id
    if anos == 1:
        an = 'ano'
    else:
        an = 'anos'
    print('Você tem {} anos, você ainda não precisa se alistar, falta {} {} para isso'.format(id, anos, an))

elif id == 18:
    print('Está na hora de você se alistar!')

elif id > 18:
    anos = id - 18
    if anos == 1:
        an = 'ano'
    else:
        an = 'anos'
    print('Você tem {} anos, já passou {} {} pra você se alistar, se já não fez, recomendo ir o mais breve possivel!'.format(id, anos, an))
