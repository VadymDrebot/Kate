print("введите целые числа для арифметических действий +,-,*,/")
while True:
    try:
         num1 = int(input("введите первое число  "))
         while True:
             try:
                 num2 = int(input("введите второе число  "))
                 print("сумма ", num1, " + ", num2, " = ", num1 + num2)
                 print("вычитание  ", num1, " - ", num2, " = ", num1 - num2)
                 print("умножение  ", num1, " * ", num2, " = ", num1 * num2)
                 if num2 != 0:
                     print("деление  ", num1, " / ", num2, " = ", num1 / num2)
                 else:
                     print("на 0 делить нельзя!!!")
                 break
             except:
                 print("Второе число введено не коректно. Попробуйте еще раз")
         break
    except:
        print("Первое число введено не коректно. Попробуйте еще раз")
        continue
#print("Завершение программы")


