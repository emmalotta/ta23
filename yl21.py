import random
num = random.randint(0, 100)
a = None
while a != num:
    a = int(input("Sisestage arvuti välja mõeldud number(0-100): "))
    if a < num:
        print("Otsitav arv on suurem")
    elif a > num:
        print("Otsitav arv on väiksem")
print("Leidsite õige numbri")
