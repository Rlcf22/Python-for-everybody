fi_le = input('Digite o nome do arquivo: ')

fhand = open(fi_le)

for line in fhand:
    line = line.upper()
    print(line)

print('Acabou!')
