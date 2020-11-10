def input_number():
    try:
        numb=int(input("введите число больше 0 "))
        return numb
    except:
        print("это не число")
        num=0
        return num

def sum_num(n):
    str_n=str(n)
    sum=0
    integer=0
    for i in str_n:
        integer=int(i)
        sum+=integer

    print("сумма ",n,"=",sum)

numb=input_number()
if numb==0:
    print("сумму не возможно посчитать или она равна 0")
else:
    sum_num(numb)


