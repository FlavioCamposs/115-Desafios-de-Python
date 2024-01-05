import datetime

print('Bem vindo a Confederação Nacional de Natação!')
ano = int(input('Diga-nos ao ano do seu nascimento para sabermos qual a sua categoria: '))

anoAtual = datetime.datetime.now().year
id = anoAtual - ano

if id <= 9:
    print('Sua idade é {}, sua categoria será MIRIM!'.format(id))
elif id > 9 and id <= 14:
    print('Sua idade é {}, sua categoria será INFANTIL!'.format(id))
elif id > 14 and id <= 19:
    print('Sua idade é {}, sua categoria será JUNIOR!'.format(id))
elif id == 20:
    print('Sua idade é {}, sua categoria será SÊNIOR!'.format(id))
elif id > 20:
    print('Sua idade é {}, sua categoria será MASTER!'.format(id))
