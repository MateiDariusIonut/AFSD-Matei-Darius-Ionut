import json
import random

with open("stock.json", "r", encoding="utf-8") as f:
    data = json.load(f)

bancnote_initiale = data["bancnote"]
produse = data["produse"]

def calculeaza_rest(suma_rest, bancnote, stoc_bancnote):

    dp = [float('inf')] * (suma_rest + 1)
    combinatii = [-1] * (suma_rest + 1)
    dp[0] = 0

    for i in range(suma_rest + 1):
        for bancnota in bancnote:
            valoare = bancnota['valoare']
            if i >= valoare and dp[i - valoare] < float('inf') and stoc_bancnote[valoare] > 0:
                if dp[i] > dp[i - valoare] + 1:
                    dp[i] = dp[i - valoare] + 1
                    combinatii[i] = valoare

    rest = suma_rest
    bancnote_utilizate = []
    while rest > 0:
        valoare_bancnota = combinatii[rest]
        if valoare_bancnota == -1:
            return None
        bancnote_utilizate.append(valoare_bancnota)
        rest -= valoare_bancnota
        if stoc_bancnote[valoare_bancnota] > 0:
            stoc_bancnote[valoare_bancnota] -= 1
    return bancnote_utilizate


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
            print(f"Au fost serviți {clienti_serviti} clienți!\n")
            print("Stocul actual al bancnotelor:")
            for valoare in sorted(stoc_bancnote.keys(), reverse=True):
                print(f"Bancnota: {valoare} RON | Stoc: {stoc_bancnote[valoare]}")
            return

simulare(1000)