puuviljad = ["Õun", "Banaan", "Pirn"]

print(puuviljad)

print("Esimene puuvili:", puuviljad[0])

puuviljad.append("Ploom")
print("Viimane puuvili:", puuviljad[len(puuviljad)-1])

puuviljad[1] = "Viinamarjad"
print(puuviljad)

if "Õun" in puuviljad:
    print("Õun on olemas.")
else:
    print("Õuna pole olemas.")

print("Listis on:", len(puuviljad),)

puuviljad.remove("Pirn")
print(puuviljad)

puuviljad.reverse()
puuviljad.sort()
print(puuviljad)