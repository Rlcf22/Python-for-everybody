fi_le = input('Digite o nome do arquivo: ')
count = 0
soma = 0
fhand = open(fi_le)

#X-DSPAM-Confidence: 0.8475 formato da linha a ser encontrada
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
       line = line.rstrip()
       count = count + 1
       dois_pontos = line.find(':')
       num_ber = line[dois_pontos+2:]
       num_float = float(num_ber)
       soma = soma + num_float

media = soma/count

print('Média de confiança de spam:',media)
