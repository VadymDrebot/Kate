def create_dict_tel_em():
    count=int(input("сколько элементов будет в словаре "))
    dict1= {}
    dict_in=dict()
    for i in range(count):
        key_name=input("введите имя\t")
        value_tel=input ("введите тел\t")
        value_email = input("введите почту\t")
        dict_in["tel"]=value_tel
        dict_in["email"]=value_email
        dict1[key_name]=dict_in

    #print(dict1)

    return dict1

def create_dict_w_h():
    count=int(input("сколько элементов будет в словаре "))
    dict1= {}
    dict_in=dict()
    for i in range(count):
        key_name=input("введите имя\t")
        value_h=input ("введите рост\t")
        value_w = input("введите вес\t")
        dict_in["height"]=value_h
        dict_in["weight"]=value_w
        dict1[key_name]=dict_in

    #print(dict1)

    return dict1

def print_table(tabl):
    print("┌───────────┬───────────┐")
    print("│ключ       │значение   │")
    for i in tabl:
        # print ("┌────────────────────┐└┘├┤┬┴┼─│")
        print("├───────────┼───────────┤")
        print("│", i, "\t\t│", tabl[i], "\t\t│")
    print("└───────────┴───────────┘")

d_tel_em=create_dict_tel_em()
d_h_w=create_dict_w_h()
name=input("введите имя ")
d_new={}
d_in={}
if name in d_tel_em:
    if name in d_h_w:
        d_in=d_tel_em[name].copy()
        d_in.update(d_h_w[name])
        d_new[name]=d_in
#a={}
#a={'tel':a['tel']}
print(d_tel_em)
print(d_h_w)
print(d_new)