import random

arvuti = random.randrange(0,100)

while(True):
    text = int(input("Arva ära mis numbri 1-100 arvuti valis: "))

    if arvuti == text:
        print("Õige!")
        break
    elif arvuti < text:
        print("Väiksem!")
    else :
        print("Suurem!")
