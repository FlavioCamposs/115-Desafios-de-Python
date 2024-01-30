from random import randint

num = (randint(1, 51), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os numeros são: ', end=' ')
for n in num:
    print(n, end=' ')

print(f'\nO maior numero da lista é: {max(num)}')
print(f'O menor numero da lista é: {min(num)}')