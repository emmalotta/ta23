a = int(input("Sisestage esimene arv: "))
b = int(input("Sisestage teine arv: "))
c = int(input("Sisestage kolmas arv: "))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)