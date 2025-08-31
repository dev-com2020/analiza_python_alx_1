owoce = ["jabłko", "banan", "gruszka"]

for owoc in owoce:
    if owoc == "banan":
        owoce.append("pomarańcza")
        print("Dodano pomarańczę")
    elif owoc == "gruszka":
        owoce.remove("jabłko")
        print("Usunięto jabłko")

print(owoce)


tajna = 7
liczba = input("Wpisz liczbę (lub wpisz 'exit' aby zakończyć): ")

while liczba != tajna:
    if liczba == "exit":
        break
    elif int(liczba) < tajna:
        print("Za mało")
    elif int(liczba) > tajna:
        print("Za dużo")
    liczba = input("Wpisz liczbę: ")