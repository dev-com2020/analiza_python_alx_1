def funkcja():
    print("Hello from funkcja!")

def dodaj():
    a = 10
    b = 20
    return a + b

def dodaj_2(a,b):
    return a + b

def dodaj_3(a=0,b=0):
    return a + b

print("Hello World")
funkcja()
print(dodaj())
print(dodaj_2(5,15))

wynik = []
wynik.extend([dodaj(),dodaj(),dodaj()])
wynik.extend([dodaj_2(5,15),dodaj_2(10,20),dodaj_2(15,25)])
wynik.extend([dodaj_3(),dodaj_3(5),dodaj_3(b=15),dodaj_3(10,20)])
print(wynik)