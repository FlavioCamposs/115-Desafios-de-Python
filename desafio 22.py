nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())

nomeJunto = nome.replace(' ', '')
print(len(nomeJunto))

print(len(nome[0:6]))