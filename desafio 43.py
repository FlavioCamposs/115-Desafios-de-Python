print('DESCUBRA O SEU IMC AQUI!')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está ABAIXO do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f}, você está no seu peso IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f}, você está no SOBREPESO!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f}, você está com OBESIDADE!'.format(imc))
elif imc >= 40:
    print('Seu IMC é de {:.1f}, você está com OBESIDADE MÓRBIDA!'.format(imc))