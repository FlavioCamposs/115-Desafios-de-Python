from .. import interface

#VERIFICAR SE O ARQUIVO EXISTE
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #TENTAR ABRIR O ARQUIVO "NOME" EM MODO DE TEXTO
        a.close()
    except FileNotFoundError: #SE O ARQUIVO NÃO FOR ENCONTRADO, SE NÃO EXISTIR
        return False
    else:
        return True


#CRIAR ARQUIVO CASO ELE NÃO EXISTA
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #PARA ESCREVER UM ARQUIVO DE TEXTO, E SE CASO ELE NÃO EXISTIR, ELE CRIA
        a.close()
    except:
        print('\033[1;91ERROR: houve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[1;92mArquivo {nome} criado com sucesso!\033[m')


#LER O ARQUIVO E MOSTRAR NA TELA (no cabeçalho)
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;91mERROR: não foi possivel ler o arquivo!\033[m')
    else:
        interface.cabecalho('\033[1;97mPESSOAS CADASTRADAS\033[m')
        print(a.read())
        '''
        ELE VAI PEGAR TODO O ARQUIVO, DO JEITO QUE ESTIVER LÁ.
        readlines() - ELE VAI PEGAR AS LINHAS DO ARQUIVO, E JOGA NUMA LISTA
        '''
    finally:
        a.close()


#INSERIR NOVOS DADOS NO ARQUIVO
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #COLOCAR COISAS DENTRO DO ARQUIVO EXISTENTE
    except:
        print('\033[1;91mERROR: não foi possivel abrir o arquivo!\033[m')
    else:
        try:
            # ESCREVER NO ARQUIVO
            a.write(f'\033[1;94mNome:\033[m \033[1;93m{nome}\033[m; \033[1;94mIdade:\033[m \033[1;93m{idade} anos\n\033[m')
        except:
            print('\033[1;91mERROR: não foi possivel escrever os dados!\033[m')
        else:
            print(f'\033[1;92mNovo registro de {nome} adcionado.\033[m')
            a.close()
