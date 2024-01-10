word = str(input("Sisestage sõna (min 7 sümbolit): "))
word = word.strip()

lenght = len(word)

if lenght >= 7 and lenght % 2 == 1:
    print(lenght // 2)
    mid = lenght // 2
    print(word[mid-1: mid+2])
else:
    print("L")



