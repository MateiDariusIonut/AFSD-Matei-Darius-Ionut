import csv

def spanzuratoarea(cuvant_cenzurat, cuvant):

    alfabet = ['e', 'a', 'i', 'r', 't', 'n', 'u', 'o', 's', 'c', 'l', 'd', 'm', 'p', 'v', 'b', 'f', 'g', 'h', 'z', 'ă', 'ș', 'ț', 'â', 'î', 'j', 'k', 'w', 'x', 'y', 'q']
    cuvant_de_ghicit = list(cuvant_cenzurat)
    nr_pasi = 0
    while "*" in cuvant_de_ghicit:
        for litera in alfabet:
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
    with open('date.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for linie in reader:
            cuvant_cenzurat, cuvant = linie
            rezultat, pasi = spanzuratoarea(cuvant_cenzurat.strip(), cuvant.strip())
            print(f"Cuvânt: {cuvant} | Ghicit: {rezultat} | Încercări: {pasi}")

if __name__ == "__main__":
    main()