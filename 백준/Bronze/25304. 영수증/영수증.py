total_price = int(input())
total_amount = int(input())

result = 0
for _ in range(total_amount):
    price, amount = list(map(int, input().split()))
    result += (price * amount)

if result == total_price:
    print("Yes")
else: print("No")