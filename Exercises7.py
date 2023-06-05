# ---------- slides 1 N1 ------
# students = ['Maria', 'Narek', 'Karen']
# grades = [1, 2, 3]
# print({i:j for i,j in zip(students, grades)})

# ---------- slides 1 N2 ------
# dic = { 
#     'Maria':1,
#     'Narek':2,
#     'Karen':3
# }
# sum = 0
# count = 0
# for i in dic:
#     sum += dic[i]
#     count += 1
#     average =  sum / count
# print(average)

# ---------- slides 1 N3 ------
# dic = { 
#     'Maria':1.0,
#     'Narek':2.0,
#     'Karen':3
# }
# sum = 0
# count = 0
# for i in dic:
#     sum += dic[i]
#     count += 1
# average =  sum / count

# for i in dic:
#     if dic[i] <= average:
#         print(f' {i} is a good student')
#     else:
#         print(f' {i} is a bad student')

# ---------- slides 1 N4 & N5 ------

# dic = { 
#     'Maria': 1.0,
#     'Narek': 2.0,
#     'Karen': 3,
#     'Koko': 5,
#     'Christi': 6
# }

# bad_students = []
# good_students = []
# for student in dic:
#     if dic[student] < 5:
#         bad_students.append(student)
#     else:
#         good_students.append(student)

# print(f'Good Students are: {good_students}')
# print(f'Bad students are: {bad_students}')

# ---------- slides 1 N6 ------

# dic = { 
#     'Maria': 1.0,
#     'Narek': 2.0,
#     'Karen': 3,
#     'Koko': 5,
#     'Christi': 6
# }

# name = input('Enter one student name:')

# for i in dic:
#     if name == i:
#         print(f'{i}: {dic[i]}')

# ---------- slides 1 N7 ------

# s = ['a','2','b','5','c','8','a','4','e','11']
# dictionary = {}

# for i in range(0, len(s), 2):
#     key = s[i]
#     value = int(s[i + 1])

#     if key in dictionary:
#         dictionary[key] += value
#     else:
#         dictionary[key] = value

# print(dictionary)

# ---------- slides 1 N8 ------
# word = input('Enter one word:')
# dictionary = {}


# for i in range(0, len(word)):
#     key = word[i]
#     value = 1
#     if key in dictionary:
#         dictionary[key] += value
#         value += 1
#     else:
#         dictionary[key] = value
# print(dictionary)

# ---------- slides 1 N9 ------

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# count = 0
# newlist = []
# for i in old_list:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

# ---------- slides 2 N1 ------

# mydict = {
#     'a': 19,
#     'c': 2,
#     'b': 15,
#     'd': 22
# }
# newdict = {}
# my_keys = sorted(mydict, key=mydict.get, reverse=True)
# my_values = sorted(mydict.values(), reverse=True)
# for i, j in zip(my_keys, my_values):
#     newdict[i] = j
# print(newdict)

# ---------- slides 2 N2 ------
# dic = { 
#     'Maria': 1.0,
#     'Narek': 2.0,
#     'Karen': 3,
#     'Koko': 5,
#     'Christi': 6
# }

# key = input('Enter key: ')
# value = input('Enter grade: ')
# value = float(value)
# dic[key] = value

# print(dic)

# ---------- slides 2 N2 ------
# dic = { 
#     'Maria': 1.0,
#     'Narek': 2.0,
#     'Karen': 3,
#     'Koko': 5,
#     'Christi': 6
# }

# name = input('Enter name to check: ')

# if name in dic:
#     print(f'{name} already in dictionary')
# else:
#     print(f'{name} is not here!')


# ---------- slides 2 N3 ------
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}

# dict3 = {}

# for i in dict1:
#     dict3[i] = dict1[i]

# for j in dict2:
#     dict3[j] = dict2[j]

# print(dict3)

# ---------- slides 2 N4 ------

# mydict = {'a':1,'b':2,'c':12}
# mult = 1
# my_values = mydict.values()
# for i in my_values:
#     mult *= i
# print(mult)

# ---------- slides 2 N5 ------

# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# my_values = sorted(mydict.values(), reverse = True)
# my_keys = sorted(mydict, key=mydict.get, reverse= True)
# newdict = {}
# for i,j in zip(my_keys, my_values):
#     newdict[i] = j

# highest_3 = dict(list(newdict.items())[:3])
# print(highest_3)


