cidade = str(input('Digite o nome da sua cidade: ')).strip() #eliminar os espaços, caso tenha

#print(cidade[:5] == 'Santo')   #se for assim, ele irá dá falso caso n esteja escrito EXATAMENTE como está aqui: Santo
print(cidade[:5].upper() == 'SANTO')

'''
Não importa o jeito que o usuário digite, ele irá
remover os espaços do inicio e do final, e irá
jogar tudo em maiusculo, caso o usuário escreva
de qualquer jeito.

OBS: Como programador, devemos sempre pensar e previnir
que o código funcione, mesmo se o usuário escrever de forma
errada
'''