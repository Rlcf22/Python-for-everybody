fi_le = input('Digite o nome do arquivo: ')

fhand = open(fi_le)

di_cio = dict()

for line in fhand:
    pa_lav = line.split()
    for i in pa_lav:
        di_cio[i] = 1

print(di_cio)
