def gaseste_cnp(cnpuri, data_nasterii):
    n = len(cnpuri)
    ok = 0
    cnp = 0
    for i in range(0,n):
        if cnpuri[i][1:7]==data_nasterii:
            ok += 1
            cnp = cnpuri[i]
            break
    if ok == 1:
        print (f"Primul CNP găsit pentru data de naștere {data_nasterii} este {cnp}.")
    else:
        print (f"Nu s-a găsit niciun CNP pentru data de naștere {data_nasterii}.")

gaseste_cnp(["1970101223456", "1980050523456", "1970101223666", "1990050523456", "2000010123456"], "970102")