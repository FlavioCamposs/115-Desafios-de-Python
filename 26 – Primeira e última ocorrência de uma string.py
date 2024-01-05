from unidecode import unidecode
#converter caracteres acentuadas para versões não acentudadas
frase = str(input('Digite uma frase: ')).lower() #posso fazer também ".lower().strip()", colocar os 2 juntos

#Contar os numeros de "a"
tirarOsAcentos = unidecode(frase)
quantidadeDeA = tirarOsAcentos.count('a')
print('A letra "A", aparece {} vezes'.format(quantidadeDeA))

#Que posição ela aparece pela primeira vez
semEspaços = frase.strip() #remover espaços vazios
print('A primeira letra "A", apareceu na posição {}'.format(semEspaços.find('a')+1))

#Que posição ela aparece pela ultima vez
print('A última letra "A", aparece na posição {}'.format(semEspaços.rfind('a')+1))
