# ----- N1 -----
# for i in range(12, 180):
#     if i % 12 == 0 and i % 15 == 0:
#         print (f'smallest number divisble by 12 and 15 is {i}')
# else:
#     print('chka')

# ----- N2 -----
# for i in range(1,101):
#     if i % 2 == 0:
#         print (f'{i} is Even')
        
#     else: 
#         print(f'{i} is Odd')

# ----- N3 -----
# n_even = 0
# n_odd = 0
# for i in range (1, 101):
#     if i % 2 == 0:
#         n_even += 1
#     else:
#         n_odd += 1

# print(f'number of even numbers = {n_even}')
# print (f'numbers of odd numbers = {n_odd}')

# ----- N4 ---
# n1 = 0
# n2 = 1
# nth = n1 + n2
# for i in range (0, 41):
#     if nth in range (0, 41):
#         nth = n1 + n2
#         n1 = n2 
#         n2 = nth 
#         print(n1)
#     else:
#         break

# ----- N5 ---

# string = input('sting = ')

# num_digits = 0 
# num_letters = 0
# for bary in string:
#     if bary.isdigit():
#         num_digits += 1
#     elif bary.isalpha():
#         num_letters += 1

# print(f'number of digits = {num_digits} \nnumber of letters = {num_letters}')

# ----- N6 ---

# num = input('tiv =')
# number = str(num)
# n1 = int(number[0])
# n2 = int(number[1])
# n3 = int(number[2])
# n4 = int(number[3])
# n5 = int(number[4])

# print(n1 + n2 + n3 +n4 + n5)

# ----- N7 ---
# number = int(input('number ='))
# factorial = 1
# if number < 0:
#     print("Factorial goyutyun chuni")
# elif number == 0:
#     print("Factorial is 1")
# else:
#     for i in range(1, number + 1):
#         factorial = factorial*i
#     print(f' {number}! = {factorial}')





