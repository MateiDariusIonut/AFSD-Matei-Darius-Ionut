def inversare_sir(sir):
    if sir == "":
        return sir
    else:
        return inversare_sir(sir[1:]) + sir[0]

print(inversare_sir("1234"))