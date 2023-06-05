# --- N63 ----
# n_numbers = 0
# summ_numbers= 0
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         print(summ_numbers / n_numbers)
#         break
#     else:
#         summ_numbers += number
#         n_numbers += 1

# --- N64 ----
# prices = [4.95, 9.95, 14.95, 19.95, 24.95]
# discount_rate = 0.60 

# print('Original Price | Discount Amount | New Price')

# for price in prices:
#     discount_amount = price * discount_rate
#     new_price = price - discount_amount
#     discount_amount = round(discount_amount, 2)
#     new_price = round(new_price, 2)
#     print(f'{price:7.2f}$       | {discount_amount:7.2f}$        | {new_price:7.2f}§')

# --- N65 ----
# print('Celsius           |      Kelvin')
# for i in range(0,100):
#     Kelvin = i + 273 
#     print(f'{i:10f}        | {Kelvin:10f}')

# --- N66 ----

# total_cost = 0
# while True:
#     price_input = input('Enter the price (or leave blank to finish): ')
#     if price_input == '':
#         break
#     price = float(price_input)
#     total_cost += price
# total_pennies = int(total_cost * 100)
# remainder = total_pennies % 5
# if remainder < 2.5:
#     amount_due = total_pennies - remainder
# else:
#     amount_due = total_pennies + (5 - remainder)
# amount_due = amount_due / 100
# print(f'Total cost: ${total_cost:.2f}')
# print(f'Amount due: ${amount_due:.2f}')

# --- N69 ----
# cost = 0
# while True:
#     age = input('Enter your age:')
#     if age == '':
#         break
#     if 0 < int(age) <= 2:
#         continue
#     elif 2 < int(age) <= 12:
#         cost += 14
#     elif 12 < int(age) <= 65:
#         cost += 23
#     else:
#         cost += 18
# print(f'Cost: ${cost:.2f}')

# --- N72 ----

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, 'Fizz-Buzz')
#     elif i % 5 == 0:
#         print(i, 'Buzz')
#     elif i % 3 == 0:
#         print(i, 'Fizz')

# --- N73 ----

# --- N75 ----

# word = input('your word:')
# new_word = word[::-1]

# if word == new_word:
#     print('your word is a polidrome')
# else:
#     print('your word is not a polidrome')

# --- N76 ----

# word = input('your word:').lower()
# word = word.replace(' ', '')
# word = word.replace(',', '')
# new_word = word[::-1]

# if word == new_word:
#     print('your word is a polidrome')
# else:
#     print('your word is not a polidrome')

# --- N83 ----

# from random import randrange
# max_value = randrange(1, 101)
# print(max_value)
# num_updates = 0
# for i in range(1, 100):
#     num_new = randrange(1, 101)
# if num_new > max_value:
#     max_value = num_new
#     num_updates = num_updates + 1
#     print(f' Updated maximal number is {num_new}')
# else:
#     print(num_new)
#     print()
#     print("The maximum value found was", max_value)
#     print("The maximum value was updated", num_updates, "times")

# --- N84 ----
# s= ''
# while True:
#     number = input('number:')
#     if number == '':
#         break
#     else:
#         for i in range(2, int(number)):
#             if int(number) % i != 0:
#                 break 
#         else:
#             s += f'{number} '
# print(s)


# bonus 1

# n = int(input('length:'))
# while True:
#     if n <= 7:
#         print('It fits the envelope')
#         break
#     else:
#         for i in range(1, int(n)):
#             n = n/2
#             break
# print(f'Page is divided {2*i} times')

# bonus 2

# x = 10
# y = 7

# while True:
#     direction = input('Enter the direction N, W, S, E:').upper()
#     if direction == 'N':
#         if (x <= 20 and x => 0) and (y <= 15 and y => 0):
#             y += 1
#         else:
#             break
#     elif direction == 'W':
#         if (x <= 20 and x => 0) and (y <= 15 and y => 0):
#             x += 1
#         else:
#             break
#     elif direction == 'S':


# x = 10
# y = 7

# while True:
#     direction = input('Enter the direction N, W, S, E:').upper()
#     if (x <= 20 and x >= 0) and (y <= 15 and y >= 0):
#         if direction == 'N':
#             y += 1
#             print(f'Coordinates are ({x}, {y})')
#         elif direction == 'W':
#             x += 1
#             print(f'Coordinates are ({x}, {y})')
#         elif direction == 'S':
#             y -= 1
#             print(f'Coordinates are ({x}, {y})')
#         elif direction == 'E':
#             x -= 1
#             print(f'Coordinates are ({x}, {y})')
#     else:
#         print(f'Coordinates are ({x}, {y})')
#         break



# mylist = ['Hello','Python','Hi','Programming', 'Programming Develope']    
# mylist.sort(key=len)           
# print(mylist[0], mylist[-1])                                                                                                                                                              

# mylist = [1,2,3,4,5]
# n = 1
# for i in mylist:
#     n *= i
# print(n)

# mylist = ['Hello','Python','Hi','Programming', 'Programming Develope'] 








