while True:
    n = int(input())
    if n >= 0 and int(n ** 0.5) ** 2 == n:
        print("Полный квадрат")
        break
    else:
        print("Не полный квадрат")