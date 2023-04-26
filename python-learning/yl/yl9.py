a = float(input("esimene külg: "))
b = float(input("teine külg: "))
c = float(input("põhja külg: "))

if a == b == c:
    print("võrdkülgne")
elif (a <= 0) or (b <= 0) or (c <= 0):
    print("pole võimalik")
elif a == b:
    print("võrdhaarne")
else:
    print("erikülgne")
