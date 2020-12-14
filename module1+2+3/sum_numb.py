def sum_n(n):
    str_n=str(n)
    sum=0
    integer=0
    for i in str_n:
        integer=int(i)
        sum+=integer

    print("сумма ",n,"=",sum)

