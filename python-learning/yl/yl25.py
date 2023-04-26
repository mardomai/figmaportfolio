dic = {
    "firstname": "Robin",
    "lastname": "Pruunlep",
    "year": "2006",
    "from": "Kuressaare",
    "dessert": "napoleoni kook"
}

print(dic.get("from"))
print(dic["from"])

dic.update({"dessert": "mannavaht" })

for x in dic.keys():
    print(x)

for y in dic.values():
    print(y)

print(dic.items())

if 'id' in dic :
    print("Yes id")
else:
    print("No id")

print(len(dic))

dic.update({"lenght": len(dic)})

dic.pop("year")

del dic
