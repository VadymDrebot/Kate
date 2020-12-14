import sum_numb

def input_number():
    try:
        numb=int(input("введите число больше 0 "))
        return numb
    except:
        print("это не число")
        num=0
        return num


numb=input_number()
if numb==0:
    print("сумму не возможно посчитать или она равна 0")
else:
    sum_numb.sum_n(numb)