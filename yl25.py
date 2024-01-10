dict = {
    "firstname" : "Emma Lotta",
    "lastname" : "Rand",
    "year" : 2003,
    "residents" : "Saaremaa",
    "dessert" : "Sokoladikook"
}

print(dict["residents"])

print(dict.get("residents"))

dict["dessert"] = "Lumepallisupp"
print(dict)

keys = dict.keys()
print(keys)

values = dict.values()
print(values)

if "isikukood" in dict:
    print("Jah isikukood on")
else:
    print("Isikukoodi pole")

print(len(dict))

dict["Height"] = 160
print(dict)

dict.pop("year")
print(dict)