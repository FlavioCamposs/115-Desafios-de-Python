palavras = ('python', 'programacao', 'linguagem', 'computacao', 'algoritmo', 'inteligencia',
            'artificial', 'dados', 'analise', 'estrutura', 'variavel', 'funcao', 'loop',
            'condicional', 'lista', 'dicionario', 'modulo', 'desenvolvimento', 'projeto', 'codigo')
for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
