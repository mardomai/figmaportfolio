import random

while True:
    valikud = ["kivi", "paper", "käärid"]
    arvuti = random.choice(valikud)
    mina = input("Sisesta oma valik (kivi, paper, käärid): ")

    if mina == arvuti:
        print("Viik!")
    elif mina == "kivi":
        if arvuti == "käärid":
            print("Sa võitsid!")
        else:
            print("Sa kaotasid!")
    elif mina == "paper":
        if arvuti == "kivi":
            print("Sa võitsid!")
        else:
            print("Sa kaotasid!")
    elif mina == "käärid":
        if arvuti == "paper":
            print("Sa võitsid!")
        else:
            print("Sa kaotasid!")
    
    uuesti = input("Mängime uuesti? (y/n): ")
    if uuesti == "n":
        break