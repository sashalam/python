# Задание к уроку 4

#4.1
#
# def zps (sal,time,bonus):
#     zp = sal * time + bonus
#     return zp
# print(f'Zarplata = {zps(int(input("Vvedite stavku:")), int(input("Vvedite vremya: ")), int(input("Vvedite bonus: ")))}')

#4.2

# list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 22, 22, 100, 109]
# list2 = [list1[i] for i in range(len(list1)) if list1[i-1]<list1[i]]
# print(list2)

#4.3

# print(list(i for i in range(20,241) if i%20==0 or i%21==0))

#4.4

# list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# list5 = []
# for i in list4:
#     if not i in list5:
#         list5.append(i)
# print(list5)
#
# ili
#
# list_nn = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# list_n = [i for i in list_nn if list_nn.count(i) < 2]
# print(list5)

#4.5

# from functools import reduce
#
# def umnozh(prev_el,el):
#     return el*prev_el
#
# new_list = [el for el in range(100,1001) if el % 2 == 0]
# print(new_list)
# print(reduce(umnozh,new_list))

4.6

from itertools import count, cycle

cc = int(input("Vvedite s kakogo chisla schitat:"))
dd = int(input("Vvedite do kakogo:"))
for el in count(cc):
    if el > dd:
        break
    else:
        print(el)


my_listx = ["alo", "ola", 3, 9, 10, ["a","b","c"]]
c = 0
for el in cycle(my_listx):
    if c >= dd:
        break
    print(el)
    c = c + 1
