# typy danych
# int - liczby całkowite

liczba = 5
liczba_2 = -11
print(liczba)
print(liczba_2)
print(liczba_2 / liczba)
print(liczba_2 // liczba)

# float - liczby zmiennoprzecinkowe

liczba3 = 3.14
liczba4 = -3.1456
print(liczba3)
print(liczba4)

# complex
liczba5 = 2 + 3j
liczba6 = -1 - 1j
print(liczba5)
print(liczba6)

# string (łańcuchy znaków)
napis1 = "Hello"
napis2 = 'World'
print(napis1)
print(napis2)

print(napis1.count('l'))
print(napis1.lower())
print(napis1.upper())
print(napis1.replace('l', 'a'))
print(napis1.split('l'))

print(napis1[0:3])  # slicing

# typ bool
prawda = True
falsz = False
print(prawda)
print(falsz)

# typ None
nic = None
print(nic)

#  typ sekwecyjny list
lista = [11, 2, 33, 4, 5]
lista.sort()
lista.sort(reverse=True)
print(lista)
lista_dziwna = [1, "dwa", 3.0, True, None]

lista_dziwna.append("nowy element")
lista_dziwna.append([6, 7, 8])
lista_dziwna.extend([66, 77, 88])
lista_dziwna.insert(1, 567)
lista_dziwna.remove(3.0)
lista_dziwna.pop(5)

print(lista_dziwna)
print(lista_dziwna[2])
print(lista_dziwna[2:5])
print(lista_dziwna[5][1])
print(len(lista_dziwna))
print(lista_dziwna.index(88))
print(lista_dziwna.count(66))
print(66 in lista_dziwna)

liczby_a = [1, 2, 3]
liczby_b = [4, 5, 6]
liczby_c = liczby_a + liczby_b
print(liczby_c * 3)

# krotka
krotka = (1, 2, 3)
print(krotka)

# set
zbior = {1, 2, 3, 2, 3, 4}
print(zbior)

# słownik
person = {"name": "Tomek", 
          "age": 30,
          "hobby": ["programowanie", "czytanie", "sport"]}
person["city"] = "Warszawa"
person["age"] = 31
print(person)
print(person["name"])
print(person["hobby"][0])