#string="hello world"
#for char in string:
#    print (char)
while True:
    try:
        number1 = int(input("Введите 1 число: "))
        while True:
            try:
                number2 = int(input("Введите 2 число: "))
                print("Введенное 1 число:", number1)
                print("Введенное 2 число:", number2)
                break
            except:
                print("Число 2 не коректное")
            #continue
        break
    except:
        print("Число 1 не коректное")
        #continue

print("Завершение программы")
#name=input("input your name  ")
#print("your name is ",name)


