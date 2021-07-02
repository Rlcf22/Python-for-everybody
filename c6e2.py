palavra = input('Digite uma palavra:\n')
letra_a_ser_contada = input('Digite a letra a ser contada:\n')


def contagem(string,letra):
    contador = 0
    for i in string:
       if i == letra:
          contador = contador + 1
    return contador

print('A palavra digitada contém a letra ', contagem(palavra,letra_a_ser_contada),' vezes.')
