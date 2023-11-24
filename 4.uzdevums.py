# Ievadam skaitli
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

# Palaižam faktoriālo vērtību
faktorials = 1

# Aprēķinam faktoriālo vērtību, izmantojot for ciklu
for i in range(1, ievaditais_skaitlis + 1):
    faktorials *= i

# Izvadam rezultātu
print("Faktoriāls no", ievaditais_skaitlis, "ir:", faktorials)