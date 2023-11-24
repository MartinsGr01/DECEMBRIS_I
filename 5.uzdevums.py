# Iegūstam pašreizējo stundu
pašreizējā_stunda = datetime.datetime.now().hour

# Atkarībā no stundas izvadam atbilstošu sveicienu
if 6 <= pašreizējā_stunda < 12:
    sveiciens = "Labrīt!"
elif 12 <= pašreizējā_stunda < 18:
    sveiciens = "Labdien!"
else:
    sveiciens = "Labvakar!"

# Izvadam sveicienu
print(sveiciens)