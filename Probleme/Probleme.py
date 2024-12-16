def insereaza_dupa_vocale(text):
    text_final=''
    vocale="AEIOUaeiou"
    for i in text:
        if i in vocale:
            text_final = text_final+i
            text_final = text_final+'*'
        else:
            text_final = text_final + i
    return text_final

print(insereaza_dupa_vocale("hello"))
