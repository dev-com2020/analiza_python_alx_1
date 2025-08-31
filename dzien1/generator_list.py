# [wyrażenie for element in sekwencja if warunek]
litery = [litera.upper() for litera in "python"]
print(litery)

cyfry = [x+100 for x in range(10) if x > 5]
print(cyfry)

# mapowanie liter na kod ASCII
kody_ascii = {litera: ord(litera) for litera in "python"}
print(kody_ascii)