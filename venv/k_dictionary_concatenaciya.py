def create_dict():
    count=int(input("сколько элементов будет в словаре "))
    dict1=dict()
    for i in range(count):
        key=input("введите ключ\t")
        value=input ("введите значение\t")
        dict1[key]=value
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

def stick_dictionary(dict1,dict2):
    dict3=dict()
    dict3=dict1.copy()
    dict3.update(dict2)
    return dict3

def find_el(dict1,key):
    if key in dict1:
        print("key=",key," value=",dict1[key])


dictionary1=dict()
dictionary1=create_dict()
dictionary2=dict()
dictionary2=create_dict()
dictionary3=stick_dictionary(dictionary1,dictionary2)
print(dictionary1)
print(dictionary2)
print(dictionary3)
k=input("введите элемент ")
find_el(dictionary3,k)



#print_table(dictionary3)





