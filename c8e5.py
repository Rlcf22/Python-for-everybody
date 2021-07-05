fi_le = input('Digite o nome do arquivo: ')
count = 0

fhand = open(fi_le)
for line in fhand:
    if line.startswith('From '):
       lin_esp= line.split()
       count = count + 1
       print(lin_esp[1])

print("There were", count, "lines in the file with From as the first word")
