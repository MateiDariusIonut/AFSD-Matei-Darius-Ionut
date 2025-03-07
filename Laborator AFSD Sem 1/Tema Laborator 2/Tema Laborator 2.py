articol = "Fie că optezi pentru o tartă crocantă sau o prăjitură pufoasă, strugurii adaugă un gust dulce-acrișor în orice desert."
jumatate1 = articol[:len(articol)//2]
jumatate2 = articol[len(articol)//2:]

jumatate1 = jumatate1.upper()
jumatate1 = jumatate1.strip()

jumatate2 = jumatate2.replace(".","")
jumatate2 = jumatate2[::-1]
x = jumatate2[0]
x = x.upper()
jumatate2 = x+jumatate2[1::]
jumatate2 = jumatate2.replace(",","")
jumatate2 = jumatate2.replace("!","")
jumatate2 = jumatate2.replace("?","")
articol=jumatate1+jumatate2
print(articol)