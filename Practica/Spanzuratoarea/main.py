import csv

def spanzuratoarea(cuvant_cenzurat, cuvant):

    alfabet = ['E', 'A', 'I', 'R', 'T', 'N', 'U', 'O', 'S', 'C', 'L', 'D', 'M', 'P', 'V', 'B', 'F', 'G', 'H', 'Z', 'Ă', 'Ș', 'Ț', 'Â', 'Î', 'J', 'K', 'W', 'X', 'Y', 'Q']
    cuvant_de_ghicit = list(cuvant_cenzurat)
    nr_pasi = 0
    while "*" in cuvant_de_ghicit:
        for litera in alfabet:x
            if litera in cuvant_de_ghicit:
                ...
            else:
                nr_pasi += 1
            if litera in cuvant:
                for i in range(len(cuvant)):
                    if cuvant[i] == litera:
                        cuvant_de_ghicit[i] = litera
            if "*" not in cuvant_de_ghicit:
                break
    return ''.join(cuvant_de_ghicit), nr_pasi

def main():
    total_pasi = 0
    with open('cuvinte_de_verificat.txt', 'r', encoding='utf-8') as f:
        lines = csv.reader(f, delimiter = ";")
        for linie in lines:
            nr,cuvant_cenzurat, cuvant = linie
            rezultat, pasi = spanzuratoarea(cuvant_cenzurat.strip(), cuvant.strip())
            total_pasi += pasi
            print(f"Cuvânt ghicit: {cuvant} | Cuvânt: {rezultat} | Încercări: {pasi}")
    print(f"Număr pași total: {total_pasi}")

if __name__ == "__main__":
    main()