def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Nie można dzielić przez zero."

def kalkulator():
    while True:
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            operacja = input("Podaj operację (+, -, *, /) lub 'q' aby wyjść: ")

            if operacja == 'q':
                print("Koniec programu.")
                break
            elif operacja == '+':
                print("Wynik: ", dodawanie(a, b))
            elif operacja == '-':
                print("Wynik: ", odejmowanie(a, b))
            elif operacja == '*':
                print("Wynik: ", mnozenie(a, b))
            elif operacja == '/':
                print("Wynik: ", dzielenie(a, b))
            else:
                print("Nieznana operacja. Spróbuj ponownie.")
        except ValueError:
            print("Błąd: Wprowadzono niepoprawne dane. Spróbuj ponownie.")

kalkulator()