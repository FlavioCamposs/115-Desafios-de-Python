import datetime

contMaior = 0
contMenor = 0
anoAtual = datetime.datetime.now().year

for i in range(1, 8):
    ano = int(input(f'Qual o ano de nascimento da {i}º pessoa? '))
    id = anoAtual - ano

    if id >= 21:
        contMaior +=1
    else:
        contMenor += 1

print('-=' * 15)
print(f'"{contMaior}" pessoas atingiram a maior idade!\nE "{contMenor}" pessoas ainda são de menor idade!')