print('Vendedor: Compre seu primeiro notebook aqui!')
print('-=' * 20)
print('Cliente: Qual o preço deste notebook? ')
print('-=' * 20)
preco = float(input('Vendedor: O preço deste notebook está por: '))
print('-=' * 20)
print('''Vendedor: Aqui está as condições:
[1] - À vista \033[1;94mdinheiro/cheque\033[m: \033[1;93m10%\033[m de desconto
[2] - À vista no \033[1;94mcartão\033[m: \033[1;93m5%\033[m de desconto
[3] - Em até \033[1;94m2x no cartão\033[m: preço normal
[4] - \033[1;94m3x ou mais\033[m no cartão: \033[1;93m20%\033[m de juros''')
print('-=' * 20)
escolha = int(input('Programa: Digite sua escolha de acordo com o numero relacionado: '))
print('-=' * 20)
if escolha == 1:
    desconto = preco - (preco * 10 / 100)
    print('Vendedor: Seu notebook de \033[1;91mR${}\033[m, ficará por \033[1;92mR${:.2f}\033[m'.format(preco, desconto))
elif escolha == 2:
    desconto = preco - (preco * 5 / 100)
    print('Vendedor: Seu notebook de \033[1;91mR${}\033[m, ficará por \033[1;92mR${:.2f}\033[m'.format(preco, desconto))
elif escolha == 3:
    parcela = preco / 2
    print('Vendedor: Seu notebook de \033[1;91mR${}\033[m, ficará por \033[1;94m2x\033[m de \033[1;92mR${:.2f}\033[m'.format(preco, parcela))
elif escolha == 4:
    print('Programa: O limite de parcelas vai até \033[1;94m12x\033[m com \033[1;93m20%\033[m juros no valor total')
    precoComJuros = preco + (preco * 20 / 100)
    numDeParcelas = int(input('Vendedor: Em quantas vezes você deseja parcelar? '))
    parcela = precoComJuros / numDeParcelas
    print('-=' * 20)
    print('Vendedor: Seu notebook de \033[1;91mR${}\033[m, ficará por \033[1;94m{}x\033[m de \033[1;92mR${:.2f}\033[m'.format(preco, numDeParcelas, parcela))