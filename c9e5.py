fi_le = input('Digite o nome do arquivo: ')

fhand = open(fi_le)

di_cio = dict()

for line in fhand:
    if line.startswith('From '):
        lin_esp = line.split()[1]
        s_chool = lin_esp[(lin_esp.find('@')+1):]
        di_cio[s_chool] = di_cio.get(s_chool,0) + 1

print(di_cio)
