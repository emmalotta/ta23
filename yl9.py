a = float(input("Sisestage kolmnurga esimese külje pikkus: "))
b = float(input("Sisestage kolmnurga teise külje pikkus: "))
c = float(input("Sisestage kolmnurga kolmanda külje pikkus: "))
if a>0 and b>0 and c>0:
    if a == b == c:
        print("Kolmnurk on võrdkülgne")
    elif a == b or a == c or b == c or b == a:
        print("Kolmnurk on võrdhaarne")
    else:
        print("Kolmnurk on erikülgne")
else:
    print("Kolmnurga külg peab olema suurem kui 0")