a, b = map(int, input().split())

# Greatest Common Divisor
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
    
# Least Common Multiple
def lcm(x, y):
    return (x * y) // gcd(x, y)

print(gcd(a, b))
print(lcm(a, b))