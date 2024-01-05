num = int(input('Deseja ver a tabuada de qual numero? '))
print(f'A tabuada do {num} é:')
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
