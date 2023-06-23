#------Slide 1
# first = ['Ani', 'Ben']
# second = [1, 2]
# mydict = dict(zip(first, second))
# print(mydict)

#------Slide 3
# def summ(n):
#     new = []
#     count = 0
#     for i in range(n):
#         if i % 3 == 0:
#             new.append(i)
#         if i % 5 == 0:
#             new.append(i)

#     for j in new:
#         count += j
#     return print(count)
# print(summ(int(input('Enter number: '))))

#------Slide 4
# import json
# s = input('Enter string: ')
# vowel = 0
# vowels = 'aeiou'

# for i in s:
#     if i in vowels:
#         vowel += 1

# with open('hello.json', 'w') as file:
#     json.dump(vowel, file)

#------Slide 5
# def line(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.read()
#             mylist = lines.split(' ')

#             mydict = {}
            
#             for i in mylist:
#                 if i in mydict:
#                     mydict[i] += 1
#                 else:
#                     mydict[i] = 1
#             print(mydict)

#     except FileNotFoundError:
#         print('File not found :(')

# line(input('Enter file name: '))

#------Slide 6

# my_list = ['a','b','a','c','b'] 

# newset = set(my_list)
# newlist = list(newset)

# print(newlist)

#------Slide 7

# def up(filename):
#     try:
#         with open(filename) as file:
#             lines = file.read()
#             mylist = lines.split('\n')
#             count_upper = 0
#             count_lower = 0
#             for i in mylist:
#                 if i[0].isupper():
#                     count_upper += 1
#                 if i[0].islower():
#                     count_lower += 1
            
#             print(f'Count for lowercase words: {count_lower}')
#             print(f'Count for uppercase words: {count_upper}')

#     except FileNotFoundError:
#         print('File nor found :(')

# up(input('Enter filename: '))

