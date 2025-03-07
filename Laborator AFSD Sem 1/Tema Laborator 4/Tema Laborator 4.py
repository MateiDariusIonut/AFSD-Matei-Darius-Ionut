# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

delimitator = " "
afisare_progres = delimitator.join(progres)
print(f'Progres: {afisare_progres}')
print(f'Incercari ramase: {incercari_ramase}')
ok=0
numar_litere_ghicite=len(cuvant_de_ghicit)

while incercari_ramase > 0 and numar_litere_ghicite != 0:
    litera = input("Scrie o litera: ")
    if len(litera)==1:
        if litera.isalpha() and litera not in litere_incercate:
            litere_incercate.append(litera)
            ok=0
            aparitii=0
            for i in range (0,len(cuvant_de_ghicit)):
                if cuvant_de_ghicit[i]==litera:
                    progres[i]=litera
                    aparitii += 1
                    ok=1
            numar_litere_ghicite = numar_litere_ghicite - aparitii
            if ok==0:
                incercari_ramase -= 1
                afisare_progres = delimitator.join(progres)
                print(f'Progres: {afisare_progres}')
                print(f'Incercari ramase: {incercari_ramase}')
            else:
                afisare_progres = delimitator.join(progres)
                print(f'Progres: {afisare_progres}')
                print(f'Incercari ramase: {incercari_ramase}')
        else:
            print("Valoarea introdusa nu este valida sau ai incercat-o deja! Introdu o alta litera.")
            afisare_progres = delimitator.join(progres)
            print(f'Progres: {afisare_progres}')
            print(f'Incercari ramase: {incercari_ramase}')
    else:
        print("Valoarea introdusa nu este valida! Introdu o alta litera.")
        afisare_progres = delimitator.join(progres)
        print(f'Progres: {afisare_progres}')
        print(f'Incercari ramase: {incercari_ramase}')

if incercari_ramase==0:
    print(f'Ai pierdut. Cuvantul era: {cuvant_de_ghicit}')
if numar_litere_ghicite==0:
    print("Felicitări! Ai ghicit cuvântul!")