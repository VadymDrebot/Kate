import random

def create_list():
    cr_list=list()
    for i in range(0,10):
        numb=random.randint(0,10)
        cr_list.append(numb)

    return cr_list

numb_list=create_list()
print("список1  ", numb_list)
i=0
y=i+1
m=len(numb_list)
lenght=len(numb_list)
#for i in range(lenght-1):
while i<lenght:
    el1 = numb_list[i]
    y = i + 1
    while y<m:
        el2=numb_list[y]
        if el1==el2:
          #  ind=numb_list.index(y)
            numb_list.pop(y)
            m=m-1
            #y=y-1
            continue
        y+=1
    i+=1
    lenght = len(numb_list)

print("список2  ", numb_list)