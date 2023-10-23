puuviljad = ["ploom", "õun", "pirn"]
print(puuviljad)
print(puuviljad[0])
puuviljad.append("greip")
print(puuviljad[3])
puuviljad[2] = "kirss"
print(puuviljad)
if "õun" in puuviljad:
    print("Õun on listis")
print(len(puuviljad))
puuviljad.remove("ploom")
print(puuviljad)
puuviljad.reverse()
puuviljad.sort()
print(puuviljad)
