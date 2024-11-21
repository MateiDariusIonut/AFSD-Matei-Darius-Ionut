def bubble_sort(lista):
    sortat = True
    while sortat:
        sortat = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                sortat = True
    return lista

print(bubble_sort([2,6,2,5,3,1,5,7,9,2]))