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