# ------ Book N35 ------

# number = int(input("number ="))
# if number % 2 == 0 :
#     print("Even")
# else:
#     print("Odd")

# ------ Book N36 ------

# dog_age= int(input("shan tariqy ="))
# if dog_age <= 2 :
#     print(f'human_age = {dog_age*10.5}')
# else:
#     print(f'human_ = {(dog_age - 2)*4 + 21}')

# ------ Book N37 ------

# letter = input("letter = ")
# if 'a' or 'e' or 'i' or 'o' or 'u' in letter :
#     print("Vowel")
# else:
#     print("Consonant")

# ------ Book N38 ------

# number = int(input("number of sides = "))
# if number == 3:
#     print("triangle")
# elif number == 4:
#     print("rectangular")
# elif number == 5:
#     print("pentagon")
# elif number == 4:
#     print("rectangular")
# elif number == 5:
#     print("Pentagon")
# elif number == 6:
#     print("Hexagon")
# elif number == 7:
#     print("Heptagon")
# elif number == 8:
#     print("Octagon")
# elif number == 9:
#     print("Nonagon")
# elif number == 10:
#     print("Decagon")
# else:
#     print("error")

#------ Book N39 ------

# month = input('month = ').lower()
# if (month == 'januar') or (month == 'march') or (month == 'mai') or (month == 'july') or (month == 'august') or (month == 'october') or (month == 'december') :    
#     print('days = 31')
# elif month == 'febuar':
#     print('days = 28 or 29')
# else:
#     print('days = 30')

#------ Book N40 ------

# decibles = float(input("decibles = "))

# if decibles == 130:
#     print("Jackhammer")
# elif decibles < 130 and decibles > 106:
#     print("between Jackhammr and Gas Lawnmower")
# elif decibles == 106:
#     print("Gas Lawnmower")
# elif decibles < 160 and decibles > 70:
#     print("betweem Gas Lawnmower and Alarm Clock")
# elif decibles == 70:
#     print("Alarm Clock")
# elif decibles < 70 and decibles > 40:
#     print (" between Alarm Clock and Quiet Room")
# elif decibles == 40:
#     print("Quiet Room")
# else:
#     print("You can't hear it")

#------ Book N41 ------

# a = int(input("a ="))
# b = int(input("b ="))
# c = int(input("c ="))

# if a == b == c :
#     print("equilateral")
# elif a == b and a != c:
#     print("isosceles")
# else:
#     print("scalene")

#------ Book N42 ------

# tone = input("tone = ")
# octave = int(input("octave = "))

# C4 = 261.63
# D4 = 293.66
# E4 = 329.63
# F4 = 349.23
# G4 = 392.00
# A4 = 440.00
# B4 = 493.88
# if tone == 'C':
#     print(f' Note = {C4*(2**(octave-4))}(Hz)')
# elif tone == 'D':
#     print(f' Note = {D4*(2**(octave-4))}(Hz)')
# elif tone == 'E':
#     print(f' Note = {E4*(2**(octave-4))}(Hz)')
# elif tone == 'F':
#     print(f' Note = {F4*(2**(octave-4))}(Hz)')
# elif tone == 'G':
#     print(f' Note = {G4*(2**(octave-4))}(Hz)')
# elif tone == 'A':
#     print(f' Note = {A4*(2**(octave-4))}(Hz)')
# elif tone == 'B':
#     print(f' Note = {B4*(2**(octave-4))}(Hz)')
# else:
#     print("Error 404 :)")

#------ Book N43 ------

# frequency = float(input("frequency = "))

# if frequency < 262.63 and frequency > 260.63:
#     print("C4!")
# elif (frequency < 294.66) and (frequency > 292.66):
#     print("D4!")
# elif (frequency < 330.63) and (frequency > 328.63):
#     print("E4!")
# elif (frequency < 350.23) and (frequency > 348.63):
#     print("F4!")
# elif (frequency < 394.00) and (frequency > 391.00):
#     print("G4!")
# elif (frequency < 441.00) and (frequency >  439.00):
#     print("A4!")
# elif (frequency < 494.88) and (frequency >  492.88):
#     print("B4!")
# else:
#     print("Error 404")

#------ Book N44 ------

# banknote = int(input("banknote = "))

# if banknote == 1 :
#     print("George Washington is watching you")
# elif banknote == 2 :
#      print("Thomas Jefferson")
# elif banknote == 5 :
#      print("Abraham Lincoln")
# elif banknote == 10 :
#      print("Alexander Hamilton")
# elif banknote == 20 :
#      print("Andrew Jackson")
# elif banknote == 50 :
#      print("Ulysses S. Grant")
# elif banknote == 100 :
#      print("Benjamin Franklin")

#------ Book N45 ------

# month = input("month =").lower()
# day = int(input("day = "))

# if (month == 'january') and (day == 1):
#     print("Yay, New Year's Day ")
# elif (month == 'july') and (day == 1):
#     print("Who knows about Canada Day")
# elif (month == 'december') and (day == 25):
#     print("Christmas Day")
# else:
#     print("Petq e gnal gorci :( ")

#------ Book N46 ------

#------ Book N47 ------
# month = input("month = ").lower()
# day = int(input("day = "))

# if (month == 'april' and day > 0) or (month == 'mai' and day > 0) or ((month == 'march' and day >=20 )) or ((month == 'june' and day < 21 )):
#     print("spring")
# elif (month == 'july' and day > 0) or (month == 'august' and day > 0) or ((month == 'september' and day < 22 )) or ((month == 'June' and  day >= 21 )):
#     print("Summer!") 
# elif (month == 'october' and day > 0) or (month == 'november' and day > 0) or ((month == 'december' and day < 21 )) or ((month == 'september' and  day >= 22 )):
#     print("Fall!") 
# elif (month == 'januar' and day > 0) or (month == 'febuar' and day > 0) or ((month == 'march' and day < 20 )) or ((month == 'december' and  day >= 21 )):
#     print("Winter!") 
# else:
#     print("chka")        

#------ Book N48 ------
# month = input("month = ").lower()
# day = int(input("day = "))

# if (month == 'december' and day >= 22) or (month == 'januar' and day <= 19):
#     print("Capricorn")
# elif (month == 'january' and day >= 20) or (month == 'febuary' and day <= 18):
#     print("Aquarius")
# elif (month == 'febuary' and day >= 19) or (month == 'march' and day <= 20):
#     print("Pisces")
# elif (month == 'march' and day >= 21) or (month == 'april' and day <= 19):
#     print("Aries")
# elif (month == 'april' and day >= 20) or (month == 'may' and day <= 20):
#     print("Taurus")
# elif (month == 'may' and day >= 21) or (month == 'june' and day <= 20):
#     print("Gemini")
# elif (month == 'june' and day >= 21) or (month == 'july' and day <= 22):
#     print("Cancer")
# elif (month == 'july' and day >= 23) or (month == 'august' and day <= 22):
#     print("Leo")
# elif (month == 'august' and day >= 23) or (month == 'september' and day <= 22):
#     print("Virgo")
# elif (month == 'september' and day >= 23) or (month == 'october' and day <= 22):
#     print("Libra")
# elif (month == 'october' and day >= 23) or (month == 'november' and day <= 21):
#     print("Scorpio")
# elif (month == 'november' and day >= 22) or (month == 'december' and day <= 21):
#     print("Sagittarius")
# else:
#     print("chka")

#------ Book N49 ------

# year = int(input("year = "))
# if (abs(year - 2000) % 12 == 0):
#     print ("dragon")
# elif (abs(year - 2001) % 12 == 0):
#     print("Snake")
# elif (abs(year - 2002) % 12 == 0):
#     print("Horse")
# elif (abs(year - 2003) % 12 == 0):
#     print("Sheep")
# elif (abs(year - 2004) % 12 == 0):
#     print("Monkey")
# elif (abs(year - 2005) % 12 == 0):
#     print("Rooster")
# elif (abs(year - 2006) % 12 == 0):
#     print("Dog")
# elif (abs(year - 2007) % 12 == 0):
#     print("Pig")
# elif (abs(year - 2008) % 12 == 0):
#     print("Rat")
# elif (abs(year - 2009) % 12 == 0):
#     print("Ox")
# elif (abs(year - 2010) % 12 == 0):
#     print("Tiger")
# elif (abs(year - 2011) % 12 == 0):
#     print("Hare")
# else:
#     print("chka")


#------ Book N50, N 52 similar, N55, 56 ------

# magnitude = float(input("magnitude ="))
# if (magnitude < 2.0):
#     print("Micro")
# elif (magnitude >= 2.0) and (magnitude < 3.0):
#     print("Very Minor")
# elif (magnitude >= 3.0) and (magnitude < 4.0):
#     print("Minor")
# elif (magnitude >= 4.0) and (magnitude < 5.0):
#     print("Light")
# elif (magnitude >= 5.0) and (magnitude < 6.0):
#     print("Moderate")
# elif (magnitude >= 6.0) and (magnitude < 7.0):
#     print("Strong")
# elif (magnitude >= 7.0) and (magnitude < 8.0):
#     print("Major")
# elif (magnitude >= 8.0) and (magnitude < 10.0):
#     print("Great")
# else: 
#     print("Meteoric")


#------ Book N51 ------

# a = float(input("a  ="))
# b = float(input("b  ="))
# c = float(input("c  ="))

# import math
# import cmath
# d = b**2-4*a*c
# discriminant = math.sqrt(abs(d))
# if d > 0:
#     print(f'root plus = {(-b + discriminant/(2*a))} , root minus = {(-b - discriminant/(2*a))}')
# elif d == 0:
#     print(f'root plus = {(-b + discriminant/(2*a))}')
# else:
#     print("chka")     

#------ Book N53 ------
# points = float(input("ponits = "))
# round(points,1)
# if (points <= 4.3) and (points > 4.0) :
#     print("A+")
# elif (points <= 4.0) and (points > 3.7):
#     print("A")
# else:
#     print("chi yndunvum")

#------ Book N54 ------
# rating = float(input("rating = "))
# r = round(rating,1)
# if r == 0.4:
#     print(f'raise = {r*2400}')
#     print("nono")
# elif r >= 0.6 :
#     print(f'raise = {r*2400}')
# else:
#     print("nono")

#------ Book N57 ------
# n_minutes = float(input("minutes="))
# n_text = float(input("text="))

# if (n_minutes <= 50) and (n_text <= 50):
#     print("cost is 15$")
# elif (n_minutes <= 50) and (n_text > 50):
#     cost = round(((15 + (n_text-50)*0.15 + 0.44)+ (15 + (n_text-50)*0.15 + 0.44)*(0.05)),2)
#     print(f'cost = {(15 + (n_text-50)*0.15 + 0.44)+ (15 + (n_text-50)*0.15 + 0.44)*(0.05)}')
#     print("cost", cost)
# elif (n_minutes > 50) and (n_text > 50):
#     cost = round(((15 + (n_text-50)*0.15 + 0.44 + (n_minutes-50)*0.25)+ (15 + (n_text-50)*0.15 + 0.44 + (n_minutes-50)*0.25)*(0.05)),2)
#     print("cost", cost)
# elif (n_minutes > 50) and (n_text <= 50):
#     cost = round(((15 + 0.44 + (n_minutes-50)*0.25)+ (15 + 0.44 + (n_minutes-50)*0.25)*(0.05)),2)
#     print("cost", cost)
# else:
#     print("nono")

#------ Book N58 ------
# year = int(input("year = "))
# if year % 400 == 0:
#     print("Leap Year")
# elif year % 100 == 0:
#     print("not leap")
# elif year % 4 == 0:
#     print("Leap Year")
# else:
#      print("not leap")

#------ Book N59 ------
#  '''3rd elif-ic heto sksum e arjeqnery chhashvel'''
# year = int(input("year = "))
# day = int(input("day = "))
# month = int(input("month in numbers = "))

# if (day <= 30) and month in (1, 3, 5, 7, 8, 10, 12):
#     print(f'date : {year}-{month}-{day + 1} ') 
# elif (day == 31) and month in (1, 3, 5, 7, 8, 10):
#     print(f'date : {year}-{month + 1}-{day - 30}')
# elif (day == 31) and (month == 12):
#     print(f'date : {year + 1}-{month - 11}-{day - 30}')
# elif (day <= 29 ) and month in (4, 6, 9, 11):
#     print(f'date : {year}-{month}-{day + 1} ')
# elif (day == 30 ) and month in (4, 6, 9, 11):
#     print(f'date : {year}-{month + 1}-{day - 29} ')
# elif (day < 27) and (month == 2):
#     print(f'date : {year}-{month}-{day + 1} ')
# elif (day == 28) and (month == 2) and (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0) :
#     print(f'date : {year}-{month}-{day + 1} ')
# elif (day == 28) and (month == 2) and (year % 400 != 0) and (year % 4 != 0):
#     print(f'date : {year}-{month + 1}-{day - 27} ')
# else:
#     print("this day is not present")

# (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0)

# '''ayl tarberak, bayc arajini mej vorn e sxal? :D'''
# year = int(input("year = "))
# day = int(input("day = "))
# month = int(input("month in numbers = "))

# if month in (1, 3, 5, 7, 8, 10, 12):
#     if day <=30:
#         print(f'date : {year}-{month}-{day + 1}')
#     elif day == 31:
#         if month == 12:
#             print(f'date: {year + 1}-1-1')
#         else:
#             print(f'date: {year}-{month + 1}-1')
# elif month in (4, 6, 9, 11):
#     if day <= 29 :
#         print(f'date: {year}-{month}-{day + 1}')
#     elif day == 30:
#         print(f'date: {year}-{month + 1}-1')
# elif month == 2:
#     if day == 28:
#         if (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0):
#             print(f'date: {year}-{month}-{day + 1}')
#         else:
#             print(f'date: {year}-{month + 1}-1')
#     elif day <= 27:
#         print(f'date: {year}-{month}-{day + 1}')
# else:
#     print("chka ays ory")

#------ Book N60 ------

# year = int(input("year = "))

# import math
# day_of_the_week = (year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) +
# math.floor((year - 1) / 400)) % 7

# if day_of_the_week == 0:
#     print("day of week for January 1 = Sunday" )
# elif day_of_the_week == 1:
#     print("day of week for January 1 = Monday" )
# elif day_of_the_week == 2:
#     print("day of week for January 1 = Tuesday" )
# elif day_of_the_week == 3:
#     print("day of week for January 1 = Wednesday" )
# elif day_of_the_week == 4:
#     print("day of week for January 1 = Thuesday" )
# elif day_of_the_week == 5:
#     print("day of week for January 1 = Friday" )
# else:
#     print("day of week for January 1 = Saturday" )

#------ Book N61 ------

# digits = int(input("digits : "))
# letters = input("letters : ").upper()

# letters_N = len(letters)
# if (digits <= 999) and (letters_N <= 3):
#     print(f' old license plate : {letters}{digits}')
# elif (digits > 999) and (letters_N <= 3):
#    print(f' new license plate : {digits}{letters}')
# else:
#    print("not registered license plate")



# license_plate = input("license plate : ").upper()
# if len(license_plate)== 6:
#    if license_plate[3:].isdigit() and license_plate[:3].isalpha():
#       print("Valid Old License plate")
#    else:
#       print("Invalid")
# elif len(license_plate)== 7:
#    if license_plate[4:].isdigit() and license_plate[:3].isalpha():
#       print("Valid New License plate")
# else:
#       print("Invalid")

#------ Book N62 ------

# from random import randrang 


