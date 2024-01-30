valores = (int(input('Digite um Numero: ')), int(input('Digite um Numero: ')), int(input('Digite um Numero: ')), int(input('Digite um Numero: ')))
print(valores.count(9)) #Quantas vezes apareceu o valor 9.
print(valores.index(3)+1) #Em que posição foi digitado o primeiro valor 3.
pares = [num for num in valores if num % 2 == 0] #Quais foram os números pares.
print(pares)
'''Para cada número na tupla valores, inclua esse
número na lista pares apenas se o número for par.'''