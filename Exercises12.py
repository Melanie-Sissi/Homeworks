# ---- from slide Lesson 30 -----

# -------------N1----------------
# class Myclass:
#     def mylistik(a,b,c):
#         mylist = []
#         for i in range(a,b +1,c):
#             mylist.append(i)
#         return mylist
    
# a = int(input('Enter starting number: '))
# b = int(input('Enter ending number: '))
# c = int(input('Enter step: '))
# my_list = Myclass
# print(my_list.mylistik(a,b,c))

# -------------N2----------------
# class Multiply:
#     def mylistik(mylist):
#         newlist = []
#         for i in range(len(mylist)-1):
#             c = mylist[i] * mylist[i+1]
#             newlist.append(c)
#         return newlist

# mylist = []   
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         mylist.append(int(number))

# my_list = Multiply
# print(my_list.mylistik(mylist))

# -------------N3----------------
# class Sentence:
#     def dictate():
#         mylist = ['Ashot', 'problem']
#         s = '_, we have a _.'
#         count_ = 0
#         for i in s:
#             if i == '_':
#                 s = s.replace('_', mylist[count_], 1)
#                 count_ += 1
#         return s
# my_list = Sentence
# print(my_list.dictate())

# -------------N4----------------
# class Gumar:
#     def mylistik(self):
#         mylist = ['anymore', 'raven', 'me', 'communicate'] 
#         mylist.sort()
#         c = len(mylist[0]) + len(mylist[-1])
#         return c
    
# my_list = Gumar()
# print(my_list.mylistik())

# -------------N5----------------
# class Index:
#     def findindex(lst, number):
#         closest_index = 0
#         min_difference = abs(number - lst[0])
        
#         for i in range(1, len(lst)):
#             difference = abs(number - lst[i])
#             if difference == 0:
#                 return i  
#             if difference < min_difference:
#                 closest_index = i
#                 min_difference = difference
                
#         return closest_index

# lst = []   
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         lst.append(int(number))
# number = int(input('Enter checknumber: '))

# my_list = Index
# print(my_list.findindex(lst, number))

# -------------N6----------------
# class Mydict:
#     def square(n):
#         newdict = {}
#         for i in range(1,n):
#             newdict[i] = i**2
#         return newdict

# n = int(input('Enter a number: '))
# mydict = Mydict
# print(mydict.square(n))

# -------------N7----------------
# class Invert:
#     def invertion():
#         mydict = {'a': '1', 'b': '2', 'c': '2' }
#         newdict = {}

#         for i in mydict:
#             if mydict[i] in newdict:
#                 if isinstance(newdict[mydict[i]], list):
#                     newdict[mydict[i]].append(i)
#                 else:
#                     newdict[mydict[i]] = [newdict[mydict[i]], i]
#             else:
#                 newdict[mydict[i]] = i

#         return  newdict
    
# my_dict = Invert
# print(my_dict.invertion())

# -------------N8----------------
# class Fibo:
#     def fib(self, n):
#         if n <= 0:
#             return []
#         elif n == 1:
#             return [0]
#         elif n == 2:
#             return [0, 1]
#         else:
#             sequence = self.fib(n-1)
#             sequence.append(sequence[-1] + sequence[-2])
#             return sequence
# n = 10
# fibonacci = Fibo()
# print(fibonacci.fib(n))









