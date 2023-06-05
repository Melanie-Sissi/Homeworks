#-----Lesson 13 - N1 ------
# num = [10,20,30,(10,20),40]
# count = 0
# for n in num:
#     if isinstance(n, tuple):
#         break  
#     count += 1
# print(count)
# --- or 
# num = [10,20,30,(10,20),40]
# count = 0
# for n in num:
#     if type(n) == tuple:
#         break  
#     count += 1
# print(count)

#-----Lesson 13 - N2 ------
# mytuble = (1,2,3,'a', 'b')
# print(mytuble[::-1])
# --- or 
# mytuble = (1,2,3,'a', 'b')
# reverse = reversed(mytuble)
# print(tuple(reverse))

#-----Lesson 13 - N3 ------
# mytuble = (1,2,3,'a', 'b')
# print(f' {len(mytuble)}')

#-----Lesson 13 - N4 ------
# mytuble = (1,2,3,'a', 'b')
# mystring = ''
# for i in mytuble:
#     if type(i) == int:
#         mystring += str(i)
#     else:
#         mystring += i
# print(mystring)
# ---chstacvac tarberak---
# mytuble = (1,2,3,'a', 'b')
# for i in mytuble:
#     if type(i) == int:
#         i = str(i)
#     else:
#         continue
# new = ' '.join(mytuble)
# print(new)

#-----Lesson 13 - N5 ------
# mytuble = (1,2,3)
# sum = 0
# for i in mytuble:
#     sum += i
# print(count)

#-----Lesson 13 - N6 ------
# mytuble = (1,2,3,'a', 'b', 'Narek')
# name = input('Enter your name: ')
# for i in mytuble:
#     if i == name:
#         print('Anuny ka!')
#         break
# else:
#     print('Anuny chka :(')

#-----Lesson 14 - N1 ------
# mylist = [1,2,3,4,5]
# sum = 0
# for i in mylist:
#     sum += i
# print(sum)

#-----Lesson 14 - N2 ------
# mylist = [1,2,3,4,5]
# mult = 1
# for i in mylist:
#     mult *= i
# print(mult)

#-----Lesson 14 - N3 ------

# mylist = ['a', 'ab', 'abc', 'abcd', 'abcde']
# mylist.sort(key = len)
# print(mylist[-1])

#-----Lesson 14 - N4 ------
# mylist = ['a', 'ab', 'abc', 'abcd', 'abcde']
# mynew = ['a', 'gdh']

# for i in mylist:
#     for j in mynew:
#         if i ==j:
#             print(True)
#         break
# else:
#     print('Not true')

#-----Lesson 15 - N2 ------
# my_list =['Hp','Asus','Dell','Mac','Lenovo'] 
# for i in my_list:
#     if i == 'Mac':
#         print(True)

#-----Lesson 15 - N3 ------
# specials = ['!', '@', '#', '$', '%', '&', '*']
# password = input('Enter your password: ')

# if len(password)< 8:
#     print('Weak password')
# else:
#     digit_count = 0
#     for d in password:
#         if d.isdigit():
#             digit_count += 1
#     if digit_count < 2:
#         print('Weak Password')
#     else:
#         specials_count = 0
#         for s in specials:
#             specials_count += 1
#         if specials_count < 2:
#             print('Weak Password')
#         else:
#             print('Strong Password')
# ----- ete chliner et 2 i paymany
# specials = ['!', '@', '#', '$', '%', '&', '*']
# password = input('Enter your password: ')
# for i in specials:
#     for n in password:
#         if n.isdigit:
#             if i in password and len(password)>8:
#                 print('Strong Password')
#         break
#     else:
#         print('Weak Password')

#-----Lesson 15 - N4 ------
# link = input('Enter your link')
# print(link.split("=")[1])

#-----Lesson 15 - N5 ------
# word = input('your word:')
# new_word = word[::-1]
# if word == new_word:
#     print('open')
# else:
#     print('trash')

#-----Lesson 15 - N6 ------
# mylist = [1,2,3,4,5,6]
# s=''
# for i in mylist:
#     if type(i) == int:
#         s += str(i)
#     else:
#         s += i
# print(s)

#-----Lesson 15 - N7 ------
# numbers = []
# for i in range(5):
#     n = int(input('5 numbers: '))
#     numbers.append(n)
# print(numbers)

# for i in numbers:
#     for j in range(2, i):
#         if i % j  == 0:
#             print(f'{i} Parz e')
#             break
#     else:
#         print(f'{i} Baxadryal e')

# -----Lesson 15 - N8 ------
# numbers = []
# for i in range(5):
#     n = int(input('5 numbers: '))
#     numbers.append(n)
# print(numbers)

# for i in numbers:
#     if i % 2 != 0:
#         numbers.remove(i)
#         print(f'New List is: {numbers}')
#         break
#     else:
#         print(f"Numbers doesn't contain any odd numbers")
#         break

# -----Lesson 15 - N9 ------
# names = []
# for i in range(5):
#     n = input('5 names: ')
#     names.append(n)
# print(names)

# n_name = input('Your name: ')
# name = input('Your desired name: ')
# for i in names:
#     if name != n_name:
#         names.remove(i)
#         print(names)
#     else:
#         print('chi kareli')
#         break

# -----Lesson 15 - N10 ------
# numbers = []
# for i in range(5):
#     n = int(input('5 numbers: '))
#     numbers.append(n)
# print(numbers)

# arajin tarberak
# for i in numbers:
#     for j in numbers:
#         if j == i:
#             numbers.remove(j)
#             print(f'{j} is removed, now our numbers are {numbers}')
#         break
# else:
#     print('Everything Okay!')
# erkrord tarberak
# for i in numbers:
#     if i == numbers[i]:
#         numbers.remove(i)
#         print(f'{i} is removed, now our numbers are {numbers}')
#     else:
#         print('Everything Okay!')
#         break
# stacvox tarberak
# new_numbers = []
# for i in numbers:
#     if i not in new_numbers:
#         new_numbers.append(i)

# numbers = new_numbers
# print(numbers)



        



