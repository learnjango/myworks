# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
# n1 = 1
# n2 = 1

# n = int(input('Type number: '))
# while n1 < n < 1000000:
#     sum = n1 + n2
#     n1 = n2
#     n2 = sum
#     print(sum)


# Найдите сумму всех чисел меньше 1000
number1 = 1
number2 = int(input('Type number: '))
row = number2 / 2
while number1 != row:
    number1 += 1
    number2 -= 1
    sum = number1 + number2
    patasxan = number1 * sum
    print(patasxan)
