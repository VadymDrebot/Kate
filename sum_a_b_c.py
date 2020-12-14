def sravnenie_ab(a,b,c):
    while a<=b:
        print("значение А=", a, " пока что не больше Б=", b)
        a += c
    print("дождались! А=", a, "больше Б=", b)

a_user=int(input("введите число А \t"))
b_user=int(input("введите число Б \t"))
c_user=int(input("введите число В \t"))

sravnenie_ab(a_user,b_user,c_user)

