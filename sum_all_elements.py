lst = []
summ = 0
while True:
    number = int(input("[+] Type number: "))
    lst.append(number)
    if number == 0:
        break

for i in lst:
    summ = summ + i
print(summ)