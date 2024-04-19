jogadores = dict()
cont = 1

while True:
    jogador = {
        'nome':str(input('Nome do jogador: ')),
        'partidas':int(input('Quantas partidas ele jogou? '))
    }

    cortadas = []
    totcort = 0
    for c in range(1, jogador['partidas']+1):
        quant = int(input(f'Quantas cortadas ele fez na {c}° partida? '))
        cortadas.append(quant)
        totcort += quant

    jogador['quantidade de Cortadas'] = cortadas
    jogador['total'] = totcort

    jogadores[f'jogador {cont}'] = jogador
    cont += 1

    pc = str(input('Deseja continuar? [S/N]: '))[0].upper()
    if pc == 'N':
        break

for chave, valor in jogadores.items():
    print(f"{chave}:")
    for chave_jogador, valor_jogador in valor.items():
        print(f"    {chave_jogador}: {valor_jogador}")
    print()