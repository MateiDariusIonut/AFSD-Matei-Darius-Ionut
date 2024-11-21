def prime_palindromuri(n):
    lista = []
    for numar in range(2,n+1):
        ok=1
        for i in range(2,(numar//2)+1):
            if numar%i==0:
                ok=0
        oglindit = 0
        cp = numar
        while cp!=0:
            oglindit = oglindit * 10 + cp%10
            cp = cp//10
        if oglindit == numar and ok==1:
            lista.append(numar)
    return lista

print(prime_palindromuri(10000))


