from program import dodaj as d
import datetime as dt
from program.person import Osoba, Chatbot

osoba1 = Osoba("Jan", "Kowalski", 30)
osoba2 = Osoba("Anna", "Nowak", 25)
osoba3 = Osoba("Piotr", "Zalewski", 40)
osoba1.przedstaw_sie()

chatbot1 = Chatbot("Chatbot", "Pierwszy", 1, 1)
chatbot1.przedstaw_sie()


print(d.dodawanie(5, 10))

czas = dt.datetime.now()

print(czas.year)
print(czas.month)
print(czas.day)
print(czas.hour)
print(czas.minute)
print(czas.second)

print(f"""
     ❗️Rok: {czas.year}, 
        Miesiąc: {czas.month}, 
         Dzień: {czas.day}, 
            
            Godzina: {czas.hour}, 
             Minuta: {czas.minute}, 
              Sekunda: {czas.second}❗️""")

dzisiaj = dt.date.today()
jutro = dzisiaj + dt.timedelta(days=1)
wczoraj = dzisiaj - dt.timedelta(days=1)
data2 = dt.date(1983, 3, 5)
roznica = dzisiaj - data2

print(f"Różnica dni: {roznica.days}❗️")
print(f"Dzisiaj jest: {dzisiaj.day}.{dzisiaj.month}.{dzisiaj.year}❗️")
print(f"Jutro będzie: {jutro.day}.{jutro.month}.{jutro.year}❗️")
print(f"Wczoraj było: {wczoraj.day}.{wczoraj.month}.{wczoraj.year}❗️")