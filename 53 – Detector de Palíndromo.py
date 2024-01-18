from unidecode import unidecode

frase = str(input('Digite uma frase: '))
fraseFormatada = unidecode(frase.replace(' ', '')).strip().lower()

#Usando apenas o if
''' 
iv = fraseFormatada[::-1]

if iv == fraseFormatada:
    print(f'A frase é um palindromo!\nFrase original: {frase}\nFrase inversa: {iv}')
else:
    print(f'A frase não é um palindromo!\nFrase original: {frase}\nFrase inversa: {iv}')
'''

#utilizando o for
inverso = ''
for letra in range(len(fraseFormatada) -1, -1, -1): #começar da ultima letra, ir até a primeira, indo de -1 em -1 (de trás pra frente)
    inverso += fraseFormatada[letra]
if inverso == fraseFormatada:
    print(f'A frase é um palindromo!\nFrase original: {frase.strip()}\nFrase inversa: {inverso}')
else:
    print(f'A frase não é um palindromo!\nFrase original: {frase.strip()}\nFrase inversa: {inverso}')