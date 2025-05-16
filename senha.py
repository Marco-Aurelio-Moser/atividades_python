#SENHA
#senha = str (input('Digite uma senha'))
#confirmação = str (input('Confirme a senha'))
#if confirmação == senha:
    #print('Acesso permitido')
#else:
   # print ('Acesso negado')

#MÉDIA DAS NOTAS
#nota1 = int (input('Digite a primeira nota'))
#nota2 = int (input('Digite a segunda nota'))
#nota3 = int (input('Digite a terceira nota'))
#media =(nota1 + nota2 + nota3) /3
#if media >=7:
 #   print ('Aprovado')
#else:
 #   print('Reprovado')

# NÚMERO EM ORDEM CONTRARIA
#numero1 = int (input('Digite o primeiro numero'))
#numero2 = int (input('Digite o segundo numero'))
#numero3 = int (input('Digite o Terceiro numero'))
#numeros = [numero1, numero2, numero3]
#numeros.sort(reverse=True)
#print('Os números em ordem decrescente são:', numeros)

#LITROS GASTOS POR VIAGEM
tempo_gasto = int (input('Quanto tempo durou a viagem (horas):'))
velocidade_media = int (input('Qual foi a velocidade media da viagem(Em km/h):'))
distancia = tempo_gasto * velocidade_media
litros = distancia /12
print(f'Seu tempo gasto foi de: {tempo_gasto}, sua velocidade foi de: {velocidade_media} hr, sua distancia foi de: {distancia}km e sua quantidade de litros gastas foi de: {litros}L')

