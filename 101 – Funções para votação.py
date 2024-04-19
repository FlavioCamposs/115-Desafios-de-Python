def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return 'VOTO NEGADO!'
    elif idade == 16 or idade == 17 or idade >= 70:
        return 'OPCIONAL!'
    else:
        return 'OBRIGATÓRIO!'


id = int(input('Digite o ano do seu nascimento: '))
print(f'Pela sua idade, seu voto é: {voto(id)}')