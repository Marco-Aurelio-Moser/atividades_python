#IDADE
idade = int(input('Qual a sua idade'))
if idade >0 and idade <12:
    print('Você é criança')

elif idade >=12 and idade <=17:
    print('Você é adolescente')


elif idade >=18 and idade <=100:
    print('Você é adulto')

else:
    print('idade invalida')
