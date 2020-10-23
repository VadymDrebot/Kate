import random
rand_list=list()
#i=0
#while i<5:
#    r=random.randint(0,10)
#    rand_list.append(r)
#   print("случайное число",r)
#    i+=1
#print(rand_list)
numb=int(input("введите число "))
for i in range(5):
    r = random.randint(0, 9)
    rand_list.append(r)
#    print("случайное число", r)
    if r==numb:
        print("число ",numb, "содержиться в списке под номером ",i+1)
print(rand_list)
print("число ",numb," повторяеться в списке ",rand_list.count(numb), " раз(а)")
#ind=1
#for i in rand_list:
#    if i==numb:
#        print("число ",numb, "содержиться в списке под номером ",ind)
#    ind += 1



