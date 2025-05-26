import random
import csv
import os
from faker import Faker

fake = Faker('ro_RO')
proportie_sex = {"B": 0.49, "F": 0.51}
indici_cifra = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
output_file = "cnp.csv"
populatie = 1000000
data = []
table_size = 1000
hash_table = {}

numar_barbati = int(populatie * proportie_sex["B"])
numar_femei = populatie - numar_barbati

# Functie care calculeaza cifra de control folosita in cnp
def cifra_control(baza_cnp):
    suma = 0
    for i in range(12):
        suma += int(baza_cnp[i]) * indici_cifra[i]
    rest = suma % 11
    if rest == 10:
        return "1"
    else:
        return str(rest)

# Functie care genereaza cnp-uri conform cerintei si le da mai departe
def genereaza_cnp(sex):
    an = random.randint(1924, 2024)
    if an < 2000:
        if sex == "B":
            s = "1"
        else:
            s = "2"
    else:
        if sex == "B":
            s = "5"
        else:
            s = "6"
    luna = random.randint(1, 12)
    if luna == 2:
        if an % 4 == 0 and (an % 100 != 0 or an % 400 == 0):
            zi = random.randint(1,29)
        else:
            zi = random.randint(1,28)
    elif luna in [1, 3, 5, 7, 8, 10, 12]:
        zi = random.randint(1, 31)
    else:
        zi = random.randint(1,30)
    judet = random.randint(1, 41)
    nnn = random.randint(1, 999)
    baza_cnp = f"{s}{an%100:02d}{luna:02d}{zi:02d}{judet:02d}{nnn:03d}"
    cifra_c = cifra_control(baza_cnp)
    return baza_cnp + cifra_c

if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    with open(output_file, "r", newline="", encoding="utf-8") as f:
        date_csv = csv.reader(f)
        data = [row for row in date_csv]
else:
    for _ in range(1000001):
        cnp = genereaza_cnp("B")
        nume = fake.name()
        data.append([cnp, nume])
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

# Functie care calculeaza indexul pentru fiecare cnp
def hash_cnp(cnp, size):
    grupuri = []
    for i in range(0, len(cnp), 3):
        grupuri.append(int(cnp[i:i + 3]))
    suma = sum(grupuri)
    return suma % size

# Functie care pune cnp-urile in tabela de hash conform indexului
def uniformizare(hash_table, cnp, nume, size):
    index = hash_cnp(cnp, size)
    if index not in hash_table:
        hash_table[index] = []
    hash_table[index].append((cnp, nume))

for row in data:
    cnp, nume = row
    uniformizare(hash_table, cnp, nume, table_size)

cnp_aleatorii = random.sample(data,1000)
medie_nr_pasi = 0

for cnp, _ in cnp_aleatorii:
    index = hash_cnp(cnp, table_size)
    if index in hash_table:
        for i, (cnp_stocat, nume_stocat) in enumerate(hash_table[index], start=1):
            if cnp_stocat == cnp:
                print(f"CNP-ul: {cnp_stocat} cu numele: {nume_stocat} a fost gasit in {i} pasi")
                medie_nr_pasi += i
                break

medie_nr_pasi //= 1000
print(f"Numarul mediu de pasi este: {medie_nr_pasi}.")