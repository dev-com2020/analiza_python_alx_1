zwierze = input("Wpisz zwierze (pies lub kot lub inne)?: ")
baza = []

if zwierze == "pies":
    print("Gratulacje - masz psa!")
    baza.append("pies")
    wiek = input("Ile ma lat Twój pies?: ")
    baza.append(int(wiek))
    kolor = input("Jaki kolor ma Twój pies?: ")
    baza.append(kolor)
elif zwierze == "kot":
    print("Masz kota!")
else:
    print("Nie masz ani psa, ani kota.")

print(baza)