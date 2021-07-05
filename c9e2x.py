fi_le = input('Digite o nome do arquivo: ')

fhand = open(fi_le)

di_cio = dict()

for line in fhand:
    if line.startswith('From '):
        lin_esp = line.split()
        for i in lin_esp:
            if (i =='Fri') or (i =='Sat') or (i =='Thu') or (i =='Tue') or (i =='Wed') or (i =='Mon') or (i =='Sun'):
                di_cio[i] = di_cio.get(i,0) + 1



print(di_cio)
