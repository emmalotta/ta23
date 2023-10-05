nimi = str(input("Sisestage oma nimi:"))
print("Tere " + nimi + "!")
elukoht = str(input("Sisestage oma elukoht: "))
if elukoht == "Saaremaa" or elukoht == "saaremaa":
    print("ÖÖÖÖÖÖÖÖÖÖ")
    vanus = int(input("Sisestage oma vanus: "))
    if vanus < 18:
        print("Olete liiga noor et autot juhtida")
    elif vanus == 18:
        print("Palju õnne täisealiseks saami puhul!")
    else:
        print("Võite autot juhtida")

else:
    vanus = int(input("Sisestage oma vanus: "))
    if vanus < 18:
        print("Olete liiga noor et autot juhtida")
    elif vanus == 18:
        print("Palju õnne täisealiseks saami puhul!")
    else:
        print("Võite autot juhtida")