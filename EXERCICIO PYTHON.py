# calcular litros da viagem
tempo_d_viagem= float(input('digite quantas horas teve a viagem: '))
velocidade= float(input('digite a velocidade aproximada: '))
distancia= tempo_d_viagem * velocidade
litros= distancia/12

print(f'a quantidade de litros utilizada foi de:{litros}')
