fhand = open('romeo.txt')

l_ista=[]

for line in fhand:
    words = line.split()
    for i in words:
        if (i in l_ista) == False : l_ista.append(i)
        else: continue

l_ista.sort()

print(l_ista)
