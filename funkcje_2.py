def suma(*cyfry):
    return sum(cyfry)

def imiona(**klucze):
    for key, value in klucze.items():
        print(f"{key}: {value}")

print(suma())
print(suma(10, 20))
print(suma(5, 15, 25))

imiona(osoba1="Kowalski", osoba2="Nowak", osoba3="Zalewski")

# lambda
wynik = lambda a, b: a + b
print(wynik(5, 10))