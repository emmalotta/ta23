a = str("03600029145")
list = []
for x in a:
    list.append(x)
print(list)

odd = int(list[0]) + int(list[2])+ int(list[4]) + int(list[6]) + int(list[8]) + int(list[10])
print(odd)

multiplyodd = odd * 3
print(multiplyodd)

even =  + int(list[1]) + int(list[3]) + int(list[5]) + int(list[7]) + int(list[9])
print(even)

oddeven = multiplyodd + even
print(oddeven)

M = oddeven % 10
print(M)

if M == 0:
    print(list.append(0))
else:
    digit = 10 - M
    list.append(digit)
    print(list)