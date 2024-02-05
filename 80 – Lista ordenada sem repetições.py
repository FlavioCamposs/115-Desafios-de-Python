valores = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > valores[-1]: #se o "n" for o primeiro da lista ou maior que o ultimo elemento
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores): #enquanto a posição for menor q comprimento da lista
            if n <= valores[pos]: #se o "n" é menor ou igual a valores na posição "pos"
                valores.insert(pos, n)
                break
            pos += 1 #para ir passando a posição

print(valores)