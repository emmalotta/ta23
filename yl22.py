import random

cont = None
while cont != "n":
    a = ["kivi", "paber", "käärid"]
    b = random.choice(a)
    kpk = str(input("Kas kivi, paber või käärid? "))
    if (kpk == "kivi" and b == "käärid") or (kpk == "paber" and b =="kivi") or (kpk =="käärid" and b =="paber"):
        print("Sa võitsid")
    elif (kpk == "kivi" and b == "kivi") or (kpk == "paber" and b =="paber") or (kpk =="käärid" and b =="käärid"):
        print("Viik")
    else:
        print("Sa kaotasid")
    cont = str(input("Kas soovid uuesti mängida?(y/n) "))
