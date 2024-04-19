from lib.interface import *
from lib.arquivo import *
from time import sleep

#criar um arquivo com esse nome, CASO ele NÃO exista
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o contéudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO', 5)
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Você saiu do sistema! Até Logo!', 1)
        break
    else:
        print('\033[1;91mError! Digite uma opção válida!\033[m')
    sleep(2)