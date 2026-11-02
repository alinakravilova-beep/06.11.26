s = input("Введите число: ")
while not s.lstrip('-').isdigit():
    s = input("Ошибка. Попробуйте еще раз. Введите число: ")
print("Введено целое число:", int(s))