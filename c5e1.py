contador = 0
soma = 0


while  True:
    numeral = input('Digite um número: ')
    if numeral == 'pronto':
        break
    try:
        n = float(numeral)
        contador = contador + 1
        soma = soma + n
        continue
    except:
        print('Entrada inválida')

try:

    print('Soma total: ',soma,'Quantidade de números digitados: ',contador,'Média: ',soma/contador)

except:
    print('Nenhum número foi digitado. Rode novamente o programa')
