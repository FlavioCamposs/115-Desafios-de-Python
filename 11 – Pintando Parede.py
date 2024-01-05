largura = float(input('Qual a largura da parede? '))
altura= float(input('Qual a altura da parede? '))
area = largura * altura
#sabendo q 1 litro de tinta faz 2m^2, então:
litrosDeTinta = area / 2
print('A parede tem uma área de {}m^2, então será preciso de {}L de tinta para cobrir toda a parede.'.format(area, litrosDeTinta))
