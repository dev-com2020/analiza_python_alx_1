x = 15
y = 20

# to są 4 niezależne warunki

if x > 5:
    print("x jest większe niż 5")

if x < 5:
    print("x jest mniejsze niż 5")

if x == 5:
    print("x jest równe 5")

if x >= 5:
    print("x jest większe lub równe 5")

# jedna instrukcja warunkowa

if x == 15:
    print("x2 jest równe 15")
elif x < 15:
    print("x2 jest mniejsze niż 15")
    if y == 20:
        print("y jest równe 20")
else:
    print("x2 jest większe niż 15")

if y > 10 and y < 30:
    print("y jest w przedziale 10-30")

wiek = 10
status = "dorosły" if wiek >= 18 else "nieletni"
print(status)