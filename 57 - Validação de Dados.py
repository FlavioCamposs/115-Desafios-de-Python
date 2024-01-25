sexo = str(input('Qual o seu sexo? [M/F]: ')).upper()
while sexo not in 'MF':
    print('Dado Inválido, tente novamente!')
    sexo = str(input('Qual o seu sexo? [M/F]: ')).upper()
print('Obrigado, tenha um bom dia!')