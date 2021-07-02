max = None
min = None


while  True:
    numeral = input('Digite um número: ')
    if numeral == 'pronto':
        break
    try:
        n = float(numeral)
        if max is None or n > max:
            max = n
        if min is None or n < min:
            min = n


    except:
        print('Entrada inválida')

if max is None or min is None :
    print('Nenhum número foi digitado. Rode novamente o programa')


else:
    print('Máximo: ',max,'Mínimo: ',min)
