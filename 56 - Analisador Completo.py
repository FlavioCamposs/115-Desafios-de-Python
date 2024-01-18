id = []
maiorIdadeHomem = 0
nomeMaisvelho = ''
totMulher20 = 0

for i in range(1, 5):
    nome = str(input(f'Digite o nome da {i}° pessoa: '))
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo [M/F]? '))
    print('-=' * 10)

    if idade:
        id.append(idade)

    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisvelho = nome

    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisvelho = nome

    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

media = sum(id) / i
print(f'A média de idade do grupo é de: {media}')
print(f'O nome de homem mais velho é: {nomeMaisvelho} e a idade dele é: {maiorIdadeHomem}')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos')

