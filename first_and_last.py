def in_digit():       # функция создает список, первый и последний элемент
    spisok=[]         # НО НЕ выводит их на экран
    print("input numbers(for quit press 'q'): ")
    x=0
    num=0
    while x!="q":
        x=input()
        try:
            spisok.append(int(x))
            num+=1
        except:
            if x!="q":
                print("please input only numbers(digits)")
    num1=spisok[0]
    num2=spisok[num-1]
    return num1,num2,spisok

print("Hello")
x,y,z=in_digit()
print("whole list: ",z)
print("first digit: ",x)
print("last digit: ",y)

