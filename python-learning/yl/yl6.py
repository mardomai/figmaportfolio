a = int(input("Esimene number:"))
b = int(input("Teine number:"))
c = int(input("Kolmas number:"))

def suurim(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest

print(suurim(a, b, c))
