# ------ Book N85 ---
# def pyth(a,b):
#     c = (a**2 + b**2)**(1/2)
#     return f' hypotenuse = {c}'
# print(pyth(int(input('Enter a: ')), int(input('Enter b: '))))

# ------ Book N86 ---
# def taxi(d):
#     base = 4.00
#     c = 0.25
#     cost = (d*(100/14))*c + base
#     return f'{cost}$ for this taxidrive'
# print(taxi(float(input('Distance in km: '))))

# ------ Book N87 ---

# def order(number):
#     first = 10.95
#     after_first = 2.95
#     charge = first + (number - 1)*after_first
#     return f'Number of items | Charge \n{number:16}| {charge}'
# print(order(int(input('Number of ordered items: '))))

# ------ Book N88 ---
# def median(n1,n2,n3):
#     mylist = []
#     mylist.append(n1)
#     mylist.append(n2)
#     mylist.append(n3)
#     mylist_sorted = sorted(mylist)
#     return f'{mylist_sorted[1]}'
# print(median(int(input('n1 = ')),int(input('n2 = ')),int(input('n3 = '))))

# ------ Book N98 ---
# def func(number):
#     for i in range(2, number):
#         return f'{number % i == 0}'
# print(func(int(input('Enter number: ' ))))

# ------ Book N99 ---
# def nextPrime(n):
#     while True:
#         n += 1
#         for i in range(2, n):
#             if n % i == 0:
#                 return f'Next prime number is {n}'
#             else:
#                 continue

# print(nextPrime(int(input('Enter number: '))))

# ------ Book N100 ---
# def password():
#     import random
#     n1 = []
#     for _ in range(10):
#         n1.append(chr(random.randint(33,126)))
#     new_list = ''.join(n1)
#     return f'Your Password is {new_list}'
# print(password())

# erkar tarberak
# def password():
#     import random
#     n1 = []
#     lengt = random.choice([10,9,8,7])
#     if lengt == 10:
#         for _ in range(10):
#             n1.append(chr(random.randint(33,126)))
#         new_list = ''.join(n1)
#         return f'Your Password is {new_list}'
#     elif lengt == 9:
#         for _ in range(7):
#             n1.append(chr(random.randint(33,126)))
#         new_list = ''.join(n1)
#         return f'Your Password is {new_list}'
#     elif lengt == 8:
#         for _ in range(7):
#             n1.append(chr(random.randint(33,126)))
#         new_list = ''.join(n1)
#         return f'Your Password is {new_list}'
#     elif lengt == 7:
#         for _ in range(7):
#             n1.append(chr(random.randint(33,126)))
#         new_list = ''.join(n1)
#         return f'Your Password is {new_list}'
# print(password())

# ------ Book N101 ---
# def license():
#     import random
#     plate = []
#     lengt = random.choice([6,7])
#     if lengt == 6:
#         for _ in range(3):
#             plate.append(chr(random.randint(97,122)))
#             plate.append(chr(random.randint(48,57)))
#         plate = ''.join(plate)
#         return f' Old License plate {plate}'
#     elif lengt == 7:
#         for _ in range(4):
#             plate.append(chr(random.randint(97,122)))
#         for _ in range(3):
#             plate.append(chr(random.randint(48,57)))
#         plate = ''.join(plate)
#         return f' New License Plate {plate}'
# print(license())
    
# ------ Book N109 ---

# def magic(day, month, year):
#     last_digits_year = str(year)[2:]
#     if day*month == int(last_digits_year):
#         return f'{day}:{month}:{year} is a magic date!'
#     else:
#         return f'{day}:{month}:{year} is not a magic date!'
# print(magic(int(input('Enter day: ')), int(input('Enter month: ')), int(input('Enter year: '))))

#------or-------
# def magic():
#     mydict = {
#         1: range(1, 32),
#         2: range(1, 29),
#         3: range(1, 32),
#         4: range(1, 31),
#         5: range(1, 32),
#         6: range(1, 31),
#         7: range(1, 32),
#         8: range(1, 32),
#         9: range(1, 31),
#         10: range(1, 32),
#         11: range(1, 31),
#         12: range(1, 32)
#     }

#     magic_dates = []
#     for year in range(1900, 2000):
#         for month in mydict:
#             for day in mydict[month]:
#                 if day * month == int(str(year)[2:]):
#                     magic_dates.append(f'{day}:{month}:{year} is a magic date!')
    
#     if magic_dates:
#         return '\n'.join(magic_dates)
# print(magic())





