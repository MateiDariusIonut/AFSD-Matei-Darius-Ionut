import math

def bubble_sort(lista):
    sortat = True
    while sortat:
        sortat = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                sortat = True
    return lista

def optimized_bubble_sort(lista):
    sortat = True
    n=len(lista)
    while sortat and n>1:
        sortat = False
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                sortat = True
        n -= 1
    return lista

def cautare_binara(lista, st, dr, x):
    while st<=dr:
        mij=st+(dr-st)//2
        if x==lista[mij]:
            return mij
        elif x>lista[mij]:
            return cautare_binara(lista,mij+1,dr,x)
        else:
            return cautare_binara(lista, st, mij-1, x)
    return -1

def cautare_exponentiala(lista,val):
    n=len(lista)
    if lista[0]==val:
        return 0
    i=1
    while i<n and lista[i]<val:
        i = i*2
    return cautare_binara(lista, i//2, min(i,n-1),val)

def cautare_salt(lista,val):
    n=len(lista)
    salt=int(math.sqrt(n))
    for i in range(0,n,salt):
        if lista[i]<val:
            st=i
        elif lista[i]==val:
            return i
        else:
            break
    for i in range(lista[st:st+salt]):
        if lista[i]==val:
            return i
    return -1

lista1=[1,2,4,7,9,11,13,17,21,24,27,29,33,37,41]
print(cautare_exponentiala(lista1,17))