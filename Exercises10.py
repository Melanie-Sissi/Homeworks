#------- Book N149 -----
# def show_head(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#             mylist = res.split('\n')
#             s = '\n'.join(mylist[:10])
#             return s
#     except FileNotFoundError:
#         return 'No file!'
# print(show_head(input('Enter file name: ')))

#------- Book N150 -----
# def show_last(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#             mylist = res.split('\n')
#             s = '\n'.join(mylist[-10:][::-1])
#             return s
#     except FileNotFoundError:
#         return 'No file!'
# print(show_last(input('Enter file name: ')))

#------- Book N151 -----
# def cat(filename, filename1, filename2):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#             mylist = res.split('\n')
#         with open(filename1, 'r') as file:
#             res1 = file.read()
#             mylist1 = res1.split('\n')
#         with open(filename2, 'r') as file:
#             res2 = file.read()
#             mylist2 = res2.split('\n')
#         return mylist + mylist1 + mylist2
#     except FileNotFoundError:
#         return 'No file!'
# print(cat(input('Enter file name: '), input('Enter file name: '), input('Enter file name: ')))

#------- Book N152 -----
# def line(filename, new):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#             mylist = res.split('\n')
#         with open(new, 'w') as file2:
#             for i in mylist:
#                 count += index(i)
#     except FileNotFoundError:
#         return 'No file!'
# print(line(input('Enter file name: ')))

#------- Book N153 -----
# def add_line_numbers(file, newfile):
#     with open(file, 'r') as file:
#         lines = file.readlines()

#     numbered_lines = []
#     line_number = 1

#     for i in lines:
#         numbered_line = f'{line_number}: {i}'
#         numbered_lines.append(numbered_line)
#         line_number += 1

#     with open(newfile, 'a') as file:
#         for i in numbered_lines:
#             file.write(i)

# add_line_numbers(input('Enter the filename: '), input('Enter the filename: '))

#------- Book N154 -----
# def line(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.read()
#             lines = lines.replace('!','')
#             mylist = lines.split('\n')
#             s = ''.join(mylist)

#             count = 0
#             common = ''
#             for char in s:
#                 if s.count(char) > count:
#                     count = s.count(char)
#                     common = char
            
#             if count > 1:
#                 return f'{common} is often'
#             else:
#                 return 'No character occurs more than once'
#     except FileNotFoundError:
#         print('No file!')

# print(line((input('Enter file name: '))))

#------- Book N155 -----
# def line(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.read()
#             lines = lines.replace('!','')
#             mylist = lines.split('\n')

#             count = 0
#             common = ''
#             for char in mylist:
#                 if mylist.count(char) > count:
#                     count = mylist.count(char)
#                     common = char
            
#             if count > 1:
#                 return f'{common} is often'
#             else:
#                 return 'No character occurs more than once'
#     except FileNotFoundError:
#         print('No file!')

# print(line((input('Enter file name: '))))

#------- Book N156 -----
# aystex vonc anem vor sharunaki myus tvery?
# def summ(n):
#     s = 0
#     try:
#         while n != '':
#             s += int(n)
#             n = input('Enter a number: ')
#         return s
#     except ValueError:
#             print('Invalid input.')


# print(summ(input('Enter a number: ')))

#------- Book N157 -----
# def grades(n):
#     mydict = {
#         1: 'A',
#         2: 'B',
#         3: 'C',
#         4: 'D',
#         5: 'E',
#         6: 'F'
#     }
#     try:
#         while True:
#             n = input('Enter a number (or leave blank to exit): ')
#             if n == '':
#                 break
#             n = int(n)
#             if n in mydict:
#                 print(mydict[n])
#             else:
#                 print('Invalid input.')
#     except ValueError:
#         print('Invalid input.')
# print(grades(int(input('Enter a number: '))))


