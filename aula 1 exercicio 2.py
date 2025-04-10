numero1 = int(input('Me diga um número'))
numero2 = int(input('Me diga o segundo número'))
if numero1 > numero2:
    print(f'O numero {numero1} é maior que {numero2}')
elif numero2 > numero1:
    print (f'O numero {numero2} é maior que {numero1}')
elif numero2 == numero1:
    print ('Os números são iguais')

