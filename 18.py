x = int(input())
k = 0
for a in range(1, int(x ** 0.5) + 1):
    for b in range(a, int(x ** 0.5) + 1):
        if a ** 2 + b ** 2 == x:
            k += 1
print(k)