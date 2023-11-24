# ievadam skaitli
lietotaja_ievade = int(input("Ievadiet skaitli: "))

# summas vērtība
summa = 0

# Izmantojot "for" ciklu, lai saskaitītu no 1 līdz lietotāja ievadītam skaitlim
for i in range(1, lietotaja_ievade + 1):
    summa += i

# Izvadam rezultātu
print("Summa no 1 līdz", lietotaja_ievade, "ir:", summa)
