fruta = input('Digite uma fruta:\n')

indice = 1

while indice <= len(fruta):
    letra = fruta[-(indice)]
    print(letra, end = (' '))
    indice = indice +1

print()
print('It´s all over!')
