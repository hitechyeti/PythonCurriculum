import math
def calculate_lcm(num1, num2):
    a=abs(num1*num2)
    b=math.gcd(num1,num2)
    c=a//b
    return int(c)
print(calculate_lcm(12,15))


def calculate_lcm(num1, num2):
    return math.lcm(num1, num2)


