aasta = int(input("Sisestage aasta: "))
if (aasta % 400 == 0):
    print(str(aasta) + " on liigaasta!")
elif (aasta % 4 == 0) and (aasta % 100 != 0):
    print(str(aasta) + " on liigaasta!")
else:
    print(str(aasta) + " on lihtaasta!")