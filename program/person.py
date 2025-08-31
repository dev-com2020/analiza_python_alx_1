class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat.")


class Chatbot(Osoba):
    def __init__(self, imie, nazwisko, wiek, wiek_chatu):
        super().__init__(imie, nazwisko, wiek)
        self.wiek_chatu = wiek_chatu

    def przedstaw_sie(self):
        # super().przedstaw_sie()
        print(f"Jestem chatbotem i mam {self.wiek_chatu} lat.")