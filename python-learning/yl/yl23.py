import random

def kaardi_jagamine():
    kaardival = ([11,2,3,4,5,6,7,8,9,10,10,10,10])
    ran_kaart = random.choice(kaardival)
    return ran_kaart

def kokku(kaardival):
    if sum(kaardival) == 21 and len(kaardival) == 2:
        return 0
    if 11 in kaardival and sum(kaardival) > 21:
        kaardival.remove(11)
        kaardival.append(1)
    return sum(kaardival)

def võrdle(dealerkaardid, kasutajakaardid):
    if kasutaja_punktid == 0:
        return "Sa võitsid Blackjackiga"
    elif dealer_punktid == 0:
        return "Dealer on Blackjack "
    elif kasutaja_punktid == dealer_punktid:
        return "Viik dealer võitis"
    elif kasutaja_punktid > 21:
        return "Sa läksid üle, dealer võitis "
    elif dealer_punktid > 21:
        return "Dealer läks üle, sa võitsid"
    elif kasutaja_punktid > dealer_punktid :
        return "Sa võitsid"
    else:
        return "Dealer võitis"

kasutaja = []
dealer = []
mäng_läbi = False

for _ in range(2):
    kasutaja.append(kaardi_jagamine())
    dealer.append(kaardi_jagamine())

kasutaja_punktid = kokku(kasutaja)
dealer_punktid = kokku(dealer)

while not mäng_läbi:
    kasutaja_punktid = kokku(kasutaja)
    arvuti_punktid = kokku(dealer)
    print(f"Sinu kaardid {kasutaja} ja sinu punktid {kasutaja_punktid}")
    print(f"Dealeri esimene kaart: {dealer[0]} ")

    if kasutaja_punktid == 0 or dealer_punktid == 0 or kasutaja_punktid > 21:
            mäng_läbi = True
    else:
        if kasutaja_punktid == 21 :
            mäng_läbi = True
        hit = input("Kirjuta 'Y' et hittida ja 'N' et seista\n").upper()
        if hit == "Y":
            kasutaja.append(kaardi_jagamine())
        elif hit == "N":
            mäng_läbi = True
        else:
            mäng_läbi = True

while dealer_punktid != 0 and dealer_punktid < 17:
    dealer.append(kaardi_jagamine())
    dealer_punktid = kokku(dealer)

print(f"Arvuti kaardid: {dealer}",)
print(f"Arvuti punktid: {dealer_punktid}")
print(võrdle(dealer_punktid, kasutaja_punktid))