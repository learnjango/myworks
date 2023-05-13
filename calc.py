num1 = int(input('Type first number: '))
num2 = int(input('Type second number: '))
sign = input('Type sign: ')
def calc(num1, num2):
    if sign == '*':
        return num1 * num2
    if sign == '/':
        return num1 / num2
    if sign == '+':
        return num1 + num2
    if sign == '-':
        return num1 - num2
    if sign == '**':
        return num1 ** num2
print(calc(num1=num1, num2=num2))