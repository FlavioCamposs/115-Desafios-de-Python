import moeda

num = int(input('Digite um preço: R$'))
print(f'Aumentando R${num} em 20% fica: R${moeda.aumentar(num)}')
print(f'Diminuindo R${num} em 10% fica: R${moeda.diminuir(num)}')
print(f'A metade de R${num} fica: R${moeda.metade(num)}')
print(f'O dobro de R${num} fica: R${moeda.dobro(num)}')