import hashlib

parola_de_ghicit = "0e000d61c1735636f561f430046be93b3d71flabbac3cd9e3f80093fdb357ad"

litere_mari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifre = "0123456789"
caractere_caractere_specialee = "!@#$"
litere_mici = "abcdefghijklmnopqrstuvwxyz"
total_apeluri_recursive = 0

def get_hash(parola):
    return hashlib.sha256(parola.encode()).hexdigest()

print(get_hash("A0!aaa"))