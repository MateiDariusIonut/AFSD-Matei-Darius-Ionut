import hashlib

parola_de_ghicit = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

litere_mari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifre = "0123456789"
caractere_speciale = "!@#$"
litere_mici = "abcdefghijklmnopqrstuvwxyz"
total_apeluri_recursive = 0

def get_hash(parola):
    return hashlib.sha256(parola.encode()).hexdigest()

# Functie care genereaza candidate conform cerintei si gaseste care dintre ele este aceeasi cu parola ce trebuie ghicita
def backtracking_parola(parola, count_litere_mari, count_cifre, count_caractere_speciale, count_litere_mici):
    global total_apeluri_recursive
    if len(parola) == 6:
        print(f"Candidată generată: {parola}")
        if count_litere_mari == 1 and count_cifre == 1 and count_caractere_speciale == 1 and count_litere_mici >= 3:
            if get_hash(parola) == parola_de_ghicit:
                print(f"Parola găsită: {parola}")
                print(f"Număr apeluri recursive: {total_apeluri_recursive}")
                exit()
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
        for char in caractere_speciale:
            backtracking_parola(parola + char, count_litere_mari, count_cifre, count_caractere_speciale + 1, count_litere_mici)
    if count_litere_mici < 3:
        total_apeluri_recursive += 1
        for char in litere_mici:
            backtracking_parola(parola + char, count_litere_mari, count_cifre, count_caractere_speciale, count_litere_mici + 1)

backtracking_parola("", 0, 0, 0, 0)