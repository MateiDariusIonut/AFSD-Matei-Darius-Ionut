import json
import random

with open("stock.json", "r", encoding="utf-8") as f:
    data = json.load(f)

bancnote_initiale = data["bancnote"]
produse = data["produse"]

# Functie care calculeaza restul folosind un numar minim de bancnote
def calculeaza_rest(suma_rest, bancnote, stoc_bancnote):

    nr_min_bancnote = [float('inf')] * (suma_rest + 1)
    ultima_bancnota = [-1] * (suma_rest + 1)
    nr_min_bancnote[0] = 0

    for i in range(suma_rest + 1):
        for bancnota in bancnote:
            valoare = bancnota['valoare']
            if i >= valoare and nr_min_bancnote[i - valoare] < float('inf') and stoc_bancnote[valoare] > 0:
                if nr_min_bancnote[i] > nr_min_bancnote[i - valoare] + 1:
                    nr_min_bancnote[i] = nr_min_bancnote[i - valoare] + 1
                    ultima_bancnota[i] = valoare

    rest = suma_rest
    bancnote_utilizate = []
    while rest > 0:
        valoare_bancnota = ultima_bancnota[rest]
        if valoare_bancnota == -1:
            return None
        bancnote_utilizate.append(valoare_bancnota)
        rest -= valoare_bancnota
        if stoc_bancnote[valoare_bancnota] > 0:
            stoc_bancnote[valoare_bancnota] -= 1
    return bancnote_utilizate

# Functie care simuleaza clienti si afiseaza pentru fiecare restul oferit cu numar minim de bancnote
# Daca restul nu se poate oferi se afiseaza atat datele actuale despre stocul bancnotelor cat si numarul de clienti serviti
def simulare(numar_clienti):
    suma_totala_incasata = 0
    clienti_serviti = 0
    stoc_bancnote = {bancnota['valoare']: bancnota['stoc'] for bancnota in bancnote_initiale}

    for _ in range(numar_clienti):
        produs_ales = random.choice(produse)
        pret_produs = produs_ales['pret']
        suma_platita = random.randint(pret_produs, pret_produs + 20)
        suma_totala_incasata += pret_produs
        suma_rest = suma_platita - pret_produs
        clienti_serviti += 1

        print(f"Clientul a ales: {produs_ales['nume']}")
        print(f"Produsul ales costă: {pret_produs} RON")
        print(f"Clientul a plătit suma de: {suma_platita} RON")

        bancnote_utilizate = calculeaza_rest(suma_rest, bancnote_initiale, stoc_bancnote)

        if bancnote_utilizate is not None:
            afisare_bancnote = ", ".join(f"{b} RON" for b in bancnote_utilizate)
            print(f"Restul pe care îl primește clientul: {suma_rest} RON")
            print(f"Restul a fost oferit folosind bancnotele: {afisare_bancnote}\n")
        else:
            print(f"Restul pe care îl primește clientul: {suma_rest} RON")
            print("Nu se poate oferi restul cu bancnotele disponibile!\n")
            print(f"Suma totala incasata este de: {suma_totala_incasata}")
            print(f"Au fost serviți {clienti_serviti} clienți!\n")
            print("Stocul actual al bancnotelor:")
            for valoare in sorted(stoc_bancnote.keys(), reverse=True):
                print(f"Bancnota: {valoare} RON | Stoc: {stoc_bancnote[valoare]}")
            return

simulare(100)