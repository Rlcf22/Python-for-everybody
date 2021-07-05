fi_le = input('Digite o nome do arquivo: ')

fhand = open(fi_le)

di_cio = dict()

for line in fhand:
    if line.startswith('From '):
        lin_esp = line.split()[2]
        di_cio[lin_esp] = di_cio.get(lin_esp,0) + 1

print(di_cio)
