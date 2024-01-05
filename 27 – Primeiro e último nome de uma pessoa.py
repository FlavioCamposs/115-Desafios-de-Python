n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() #dividir em listas
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
#o Len irá acessar o último elemento
#se len(nome) é 5, então len(nome) - 1 é 4, e nome[4] representa o quinto elemento da lista (o último)

print('Ultimo nome: {}'.format(nome[-1]))
#forma simplificada de pegar o último elemento, "-1" -> último, "-2" -> penultimo e etc...
