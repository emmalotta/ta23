# ( up #
# ) down #


fail = open("asi.txt")

a = fail.read()

x = 0
for c in a:
    while x >= 0:
        if c == "(":
            x += 1
        else:
            x -= 1
        
print(x)
print("läbi")
