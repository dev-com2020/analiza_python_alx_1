def formatowanie():
    """
    Funkcja do formatowania tekstu.
    Zwraca sformatowany tekst.
    Nie zawiera argumentów.
    """
    return "Formatowanie tekstu w Pythonie"

imie = "Jan"
nazwisko = "Kowalski"
wiek = 30
pi = 3.14159265
tekst = "Python"

print(f"Imię: {imie}")
print(f"Nazwisko: {nazwisko}")
print(f"Wiek: {wiek}")
print(f"Imię: {imie}, Nazwisko: {nazwisko}, Wiek: {wiek}")
print(f"Pi: {pi}")
print(f"Pi (2 miejsca po przecinku): {pi:.2f}")
print(f"Tekst: {tekst}")
print(f"Tekst: {tekst:>10}")  # Wyrównanie do prawej
print(f"{tekst:<10} jest wyrównany do lewej")  # Wyrównanie do lewej
print(f"{tekst:^10} jest wyśrodkowany")  # Wyśrodkowanie

formatowanie()