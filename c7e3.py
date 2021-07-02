fi_le = input('Digite o nome do arquivo: ')
count = 0

try:
   fhand = open(fi_le)

   for line in fhand:
       count = count +1
   print('Há',count,'linhas de assunto em',fi_le)

except:
    if fi_le == 'na na boo boo':
        print('NA NA BOO BOO PRA VOCÊ TAMBÉM!')


    else:
        print('Arquivo não pode ser aberto:',fi_le)
