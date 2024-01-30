extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove",
"Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        print(
            f'O numero digitado foi {extenso[num]}')  # ele vai escrever a string relacionada ao numero (índice) q for digitado
        pc = str(input('Quer continuar? [S/N] ')).upper()
        if pc == 'N':
            print('Você saiu!!')
            break
    else:
        print('Numero inválido!')