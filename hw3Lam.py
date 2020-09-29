# Задание к уроку 3

#3.1
# def chastnoe(d_moe, d_tel):
#     if d_tel == 0:
#         print("delit na 0 nelzya")
#     else:
#         res = d_moe / d_tel
#         return print(res)
# d1 = float(input("Delimoe= "))
# d2 = float(input("Delitel= "))
# chastnoe(d1,d2)

#3.2

# def info(name ='None', surname = 'None', year = 'None', city = 'None', mail = 'None', phone = 'None'):
#     i = [name, surname, year, city, mail, phone]
#     return print(i)
# imya = str(input("Vvedite imya: "))
# fam = str(input("Vvedite familiu: "))
# god = int(input("Vvedite god rozhdenia: "))
# gorod = str(input("Vvedite gorod: "))
# pochta = str(input("Vvedite pochtu: "))
# tel = int(input("Vvedite telefon: "))
#
# info(name = imya, surname = fam, year = god, city = gorod, mail = pochta, phone = tel)

# 3.3

# def my_func(x1 , x2, x3):
#     if x1 >= x3 and x2 >= x3:
#         return x1 + x2
#     elif x1 >= x2 and x2 <= x3:
#         return x1 + x3
#     else:
#         return x2 + x3
#
# print(f'summa 2-ikh chisel = {my_func(int(input("x1= ")), int(input("x2= ")), int(input("x3= ")))}')

# 3.4
# def my_func(x, y):
#     x0 = x
#     for i in range((-1)*y-1):
#         x0 = x0*x
#     return 1/x0
#
#
# print(f'Rezultat = {my_func(int(input("Vvedite chislo:")), int(input("Vvedite otrizatelnuyu stepen: ")))}')

# 3.5

# summa = 0
# cont = False
# while cont == False:
#     lst = input("Type 'S' to stop or Type numbers = ").split()
#     print(lst)
#     for i in lst:
#         if i == "S":
#             cont = True
#             break
#         else:
#             summa = summa + int(i)
#             print("Current sum",summa)
#     print("Total sum",summa)


3.6

def int_func(t):
    return t.title()

print(f'{int_func(str(input("Vvedite: ")))}')

