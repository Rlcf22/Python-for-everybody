l_st = []

while True:
     k = input('Digite um elemento da lista: ')
     if k == 'pronto': break
     l_st.append(k)

def meio(listilha):
    listilha.pop(0)
    listilha.pop(-1)
    return listilha #without this, the function returns None

print('Lista sem o primeiro e o último termo:', meio(l_st))
