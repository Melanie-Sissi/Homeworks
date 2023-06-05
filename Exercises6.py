
#-------Book N113 -----
# mylist = []
# while True:
#     word = input('Enter the word: ')
#     if word == '':
#         break
#     else:
#         mylist.append(word)
#         new_list = []
#         for i in mylist:
#                 if i not in new_list:
#                     new_list.append(i)
# print(new_list)

#-------Book N114 -----
# mynumbers = []
# while True:
#     number = input('Enter your number: ')
#     if number == '':
#         break
#     else:
#         mynumbers.append(int(number))
#         mynumbers.sort()
# print(mynumbers)

#-------Book N115 -----
# vonc anem verjum mist chberi else -i  print y
# number = int(input('Enter a positive number: '))
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(f'Your devisors are {i}')
# else:
#     print('No other devisor found :(')


# -------Book N116 -----
# number = int(input('Enter a positive number: '))
# sum = 0
# for i in range(1, number):
#     if number % i == 0:
#         sum += i
#         if sum == number:
#             print('perfect number yay')
#             break
# else:
#     print('not so perfect')

# -------Book N117 -----
# word = input('Enter your words')
# marks = [',', '!', '?',':']
# word = word.split(' ')
# new = []
# for i in range(len(word)):
#     for j in marks:
#             if word[i].endswith(j):
#                 word[i]= word[i].replace(j, '')
# print(word)

# -------Book N118 -----

# word = input('your word: ').lower()
# word = word.replace(',', '')
# mylist = word.split(' ')
# other_list = mylist[::-1]
# print(other_list)

# if mylist == other_list:
#     print('polidromeee')
# else:
#     print('not')

# -------Book N119 -----
# numbers = []
# total = 0

# while True:
#     number = input('Enter a number: ')
#     if number == '':
#         break
#     numbers.append(float(number))
#     total += float(number)

# average = total / len(numbers)
# print(f'Average value: {average}')

# for num in numbers:
#     if num < average:
#         print(f'Below average values: {num}')
#     elif num == average:
#         print(f'Average values: {num}')
#     else:
#         print(f'Above average values: {num}')

# -------Book N125 -----
# import random
# card_value =  ['2','3','4','5','6','7','8','9','T','J','Q','A']
# card_suit = ('s', 'h', 'd', 'c')
# desk = [i+j for i in card_value for j in card_suit]
# new_desk = list(random.sample(desk, len(desk)))
# print(new_desk)

# -------Book N126 -----

# -------Book N133 -----
# larger_list = [1, 2, 3, 4]
# sublist = [2, 3]

# for i in range(len(larger_list)):
#     if larger_list[i:i+len(sublist)] == sublist:
#         print('sublist found!')
#         break
# else:
#     print('sublist not found!')

# -------Book N134 -----

# larger_list = [1, 2, 3, 4]
# sublists = []
# for j in range(1, len(larger_list) + 1):
#     for i in range(len(larger_list)+ 1 - j ):
#         sublist = larger_list[i: i + j]
#         sublists.append(sublist)
# print(sublists)
