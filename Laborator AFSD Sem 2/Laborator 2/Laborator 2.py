import hashlib

parola_de_ghicit = "2fb82906d2cd83ef58aa8f30e2b67e3515f647d9177f87211d137f6796691e9b"

litere_mari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifre = "0123456789"
caractere_caractere_specialee = "!@#$"
litere_mici = "abcdefghijklmnopqrstuvwxyz"
total_apeluri_recursive = 0

def get_hash(parola):
    return hashlib.sha256(parola.encode()).hexdigest()

def backtracking_parola(parola, count_litere_mari, count_cifre, count_caractere_speciale, count_litere_mici):
    global total_apeluri_recursive
    print(f"Candidată generată: {parola}")
    if len(parola) == 6:
        if count_litere_mari == 1 and count_cifre == 1 and count_caractere_speciale == 1 and count_litere_mici >= 3:
            if get_hash(parola) == parola_de_ghicit:
                print(f"Parola găsită: {parola}")
                print(f"Număr apeluri recursive: {total_apeluri_recursive}")
                exit()
        return
    if count_litere_mari < 1:
        total_apeluri_recursive += 1
        for char in litere_mari:
            backtracking_parola(parola + char, count_litere_mari + 1, count_cifre, count_caractere_speciale, count_litere_mici)
    if count_cifre < 1:
        total_apeluri_recursive += 1
        for char in cifre:
            backtracking_parola(parola + char, count_litere_mari, count_cifre + 1, count_caractere_speciale, count_litere_mici)
    if count_caractere_speciale < 1:
        total_apeluri_recursive += 1
        for char in caractere_caractere_specialee:
            backtracking_parola(parola + char, count_litere_mari, count_cifre, count_caractere_speciale + 1, count_litere_mici)
    if count_litere_mici < 3:
        total_apeluri_recursive += 1
        for char in litere_mici:
            backtracking_parola(parola + char, count_litere_mari, count_cifre, count_caractere_speciale, count_litere_mici + 1)

backtracking_parola("", 0, 0, 0, 0)