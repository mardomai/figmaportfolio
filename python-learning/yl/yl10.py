name = input("Mis su nimi on?: ")

print("Tere",name,)

elukoht = input("Kus sa elad?: ")

if elukoht == "Saaremaa":
    print("Põder pani põmmdi põõsase!")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Liiga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne täisealiseks saamisel!")
elif age > 18:
    print("Võid autot juhtida.")