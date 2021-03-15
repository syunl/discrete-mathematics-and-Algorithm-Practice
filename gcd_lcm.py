def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


def lcm(x, y):
    g = gcd(x, y)
    result = x * y / g
    return result


print(lcm(15, 10))
print(lcm(12, 20))
