import time
import random

nimi = input("Tere, mis su nimi on? ")

time.sleep(1)
print("Tere " + nimi)

today = input("Kuidas sul täna läinud on? ")
if "hästi" in today:
    print("Tore sama siin! ")
elif "halvasti" in today:
    input("Oi mis juhtus? ")
    
