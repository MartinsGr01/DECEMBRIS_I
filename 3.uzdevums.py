# Ievadam skaitli
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

# Pārbaudam, vai skaitlis dalās ar 3 un 7
if ievaditais_skaitlis % 3 == 0 and ievaditais_skaitlis % 7 == 0:
    print(ievaditais_skaitlis, "dalās ar 3 un 7.")
else:
    print(ievaditais_skaitlis, "nedalās ar 3 un 7.")