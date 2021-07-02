fruta = input('Digite uma fruta:\n ')

indice = 1

while indice <= len(fruta):
    letra = fruta[-(indice)]
    print(letra)
    indice = indice +1

print('It´s all over!')
