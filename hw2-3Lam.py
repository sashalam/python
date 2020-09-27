#Задание к уроку 2
#1
list1 = ['Moscow', 23, 1.5, 'Kiev', ['hello'], ('what', 'is', 'your', 'name' )]
print(list1)
for i in list1:
    print (i, type(i))


#3
dict1 = {
    1: "Winter",
    2: "Winter",
    3: "Winter",
    4: "Spring",
    5: "Spring",
    6: "Spring",
    7: "Summer",
    8: "Summer",
    9: "Summer",
    10: "Autumn",
    11: "Autumn",
    12: "Autumn",
}
print(dict1)
a = int(input("Vvedite chislo ot 1 do 12: "))
if a <= 12 and a >=1:
    print(a, dict1[a])
else:
    print("Net takogo mesyaza")

#4
line = str(input("Your sentence: "))
new_list = line.split()
k = len(new_list)
print('Elementov v spiske: ', k)
for i, element in enumerate(new_list):
    print(i + 1, element[0:10])

#5
my_list = [7, 5, 3, 3, 2]
my_list2 = my_list [:]
num = int(input('Vvedite naturalnoe chislo: '))
if num <= min (my_list):
    my_list2.append(num)
    print(my_list2)
else:
    while num <= max(my_list):
        my_list.remove(max(my_list))
    maks = max(my_list)
    ind2 = my_list2.index(maks)
    my_list2.insert(ind2, num)
    print(my_list2)


