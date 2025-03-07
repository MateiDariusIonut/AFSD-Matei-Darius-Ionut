meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

while studenti:
    print(studenti[0] + " a comandat " + comenzi[0])
    studenti.pop(0)
    tavi.pop()
    istoric_comenzi.append(comenzi[0])
    meniu.remove(comenzi[0])
    comenzi.pop(0)

nr_comenzi_guias = istoric_comenzi.count('guias')
nr_comenzi_ceafa = istoric_comenzi.count('ceafa')
nr_comenzi_papanasi = istoric_comenzi.count('papanasi')
print ('S-au comandat ' + str(nr_comenzi_guias) + ' guias, ' + str(nr_comenzi_ceafa) + ' ceafa, ' + str(nr_comenzi_papanasi) + ' papanasi.' )
nr_tavi_ramase = tavi.count('tava')
print ('Mai sunt ' + str(nr_tavi_ramase) + ' tavi.')
print ('Mai este ceafa:', 'ceafa' in meniu)
print ('Mai este papanasi:', 'papanasi' in meniu)
print ('Mai este guias:', 'guias' in meniu)

venit_total = nr_comenzi_guias*preturi[2][1] + nr_comenzi_ceafa*preturi[1][1] + nr_comenzi_papanasi*preturi[0][1]
print ('Cantina a incasat: ' + str(venit_total) + ' lei.')

produse=[]
if preturi[0][1] <= 7:
    produse.append(preturi[0])
if preturi[1][1] <= 7:
    produse.append(preturi[1])
if preturi[2][1] <= 7:
    produse.append(preturi[2])
print(produse)