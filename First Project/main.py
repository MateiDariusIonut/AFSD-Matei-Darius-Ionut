import random

numar = random.randint(1,10)
ghicit = 0
print("M-am gandit la un numar, incearca sa-l ghicesti!")

while ghicit != numar:

    ghicit = int(input("Ghiceste numarul: "))

    if ghicit < numar:
        print("Mai mare")
    elif ghicit > numar:
        print("Mai mic")
    else:
        print("Ai ghicit!")
