# ----- Bok N136 ----
# myset = {1,2,3,4,5,6,7}
# number = int(input('Enter number: '))

# for i in myset:
#     if i == number:
#         print(f'{number} is in myset!')
#         break
# else:
#     print('Try again :(')

# ----- Bok N137 ----
# import random
# frequencies = {}
# for _ in range(1000):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice1 + dice2
#     frequencies[total] = frequencies.get(total, 0) + 1
# print('Total\tFrequency')
# for total in range(2, 13):
#     frequency = frequencies.get(total, 0)
#     print(f'{total}\t{frequency}')

# ----- Bok N139 ----
# text = input('Enter text: ').upper()
# mydict = {
#     'A':'.-',
#     'B':'-...',
#     'C':'-.-.',
#     'D':'-..',  
#     'E':'.', 
#     'F':'..-.', 
#     'G':'- -.', 
#     'H':'....', 
#     'I':'..', 
#     'J':'.- - -',
#     'K':'-.-',
#     'L':'.-..',
#     'M':'- -',
#     'N':'-.',
#     'O':'---',
#     'P':'.- -.',
#     'Q':'- -.-',
#     'R':'.-.',
#     'S':'...',
#     'T':'-',
#     'U':'..-',
#     'V':'...-',
#     'W':'.- -',
#     'X':'-..-',
#     'Y':'-.- -',
#     'Z':'- -..'
# }

# for i in text:
#     if i in mydict:
#         morse = mydict[i]
#         print(f'{morse}', end='')

# ----- Book N140 ----

# mydict = {
#     'A': 'Newfoundland',
#     'B': 'Nova Scotia',
#     'C': 'Yerevan',
# }
# code = input('Enter your code: ')
# for i in code:
#     if i in mydict:
#         adress = mydict[i]
#         if i == '0':
#             print(f'Rural')
#         else:
#             print('Urban')
# print(f'{adress}')

# ----- Book N141 ----
# number = int(input('Number: '))

# mydict1 = {
#     1: 'One',
#     2: 'Two',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five',
#     6: 'Six',
#     7: 'Seven',
#     8: 'Eigt',
#     9: 'Nine',
#     10: 'Ten',
#     11: 'Eleven',
#     12: 'Twelve',
#     13: 'Thirdteen',
#     14: 'Fourteen',
#     15: 'Fifthteen',
#     16: 'Sixteen',
#     17: 'Seventeen',
#     18: 'Eigteen',
#     19: 'Nineteen'
# }
# mydict2 = {
#     20: 'Twenty',
#     30: 'Thirty',
#     40: 'Fourty',
#     50: 'Fifty',
#     60: 'Sixty',
#     70: 'Seventy'
# }

# number_decimal = int(str(number)[:-1] + '0')
# number_small = number - number_decimal

# for i in mydict2:
#     if i == number_decimal:
#         english = mydict2[i]

# for j in mydict1:
#     if j == number_small:
#         english_1 = mydict1[j]

# print(f'{english} {english_1}')

# ----- Book N141 ----
# word = input('Enter your text: ')
# word = word.replace(' ','')
# mydict = {}
# for i in word:
#     mydict[i] = word.count(i)
# print(f'Unique Characters: {len(mydict)}')

# ----- Book N142 ----
# word1 = input('Enter the first word: ').lower()
# word2 = input('Enter the second word: ').lower()

# if len(word1) != len(word2):
#     print('Not anagrams')
# else:
#     sorted_word1 = sorted(word1)
#     sorted_word2 = sorted(word2)

#     if sorted_word1 == sorted_word2:
#         print('Anagrams')
#     else:
#         print('Not anagrams')

# ----- Book N143 ----
# word1 = input('Enter the first word: ').lower()
# word2 = input('Enter the second word: ').lower()
# word1 = word1.replace(' ','')
# word2 = word2.replace(' ','')

# if len(word1) != len(word2):
#     print('Not anagrams')
# else:
#     sorted_word1 = sorted(word1)
#     sorted_word2 = sorted(word2)

#     if sorted_word1 == sorted_word2:
#         print('Anagrams')
#     else:
#         print('Not anagrams')

# ----- Book N144 ----
# mydict = {
#     1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
#     2: ['D','G'],
#     3: [ 'B', 'C', 'M' ,'P']
# }

# word = input('Enter your word: ').upper()
# value = 0
# for i in word:
#     for j in mydict:
#         if i in mydict[j]:
#             value += j
# print(f'Scramble score is: {value}')

# ----- Book N145 ----
# import random
# number1 = []
# number2 = []
# number3 = []
# number4 = []
# number5 = []
# bingo = {
#     'b': [],
#     'i': [],
#     'n': [],
#     'g': [],
#     'o': []
# }
# for i in range(5):
#     x = random.randint(1,15)
#     number1.append(x)
#     y = random.randint(16,30)
#     number2.append(y)
#     z = random.randint(31,45)
#     number3.append(z)
#     m = random.randint(46,60)
#     number4.append(m)
#     n = random.randint(61,75)
#     number5.append(n)

# bingo['b'] = number1
# bingo['i'] = number2
# bingo['n'] = number3
# bingo['g'] = number4
# bingo['o'] = number5
    

# for i in bingo:
#     print(f'{i}:{bingo[i]}')



