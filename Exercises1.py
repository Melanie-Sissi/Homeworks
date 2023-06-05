# # ----- Book N11 ------

# MPG = float(input("MPG = "))
# LPH = MPG * 235.215
# print(f'LPH = {LPH}, (L/100 km)')

# ----- Book N12 ------

# t1 = float(input("Latitual point 1 = "))
# t2 = float(input("Latitual point 2 = "))
# g1 = float(input("Longtitutal point 1 = "))
# g2 = float(input("Longtitutal point 2 = "))

# import math

# distance =  6371.01 *math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos((g1 - g2)))

# print('distance =', distance)

# ----- Book N13 ------

# CENTS_PER_TOONIE = 200
# CENTS_PER_LOONIE = 100
# CENTS_PER_QUARTER = 25
# CENTS_PER_DIME = 10
# CENTS_PER_NICKEL = 5

# cents = int(input("Enter cents: ")

# print(" ", cents // CENTS_PER_TOONIE, "toonies")
# cents = cents % CENTS_PER_TOONIE

# print(" ", cents // CENTS_PER_LOONIE, "loonies")
# cents = cents % CENTS_PER_LOONIE

# print(" ", cents // CENTS_PER_QUARTER, "quarters")
# cents = cents % CENTS_PER_QUARTER

# print(" ", cents // CENTS_PER_DIME, "dimes")
# cents = cents % CENTS_PER_DIME

# print(" ", cents // CENTS_PER_NICKEL, "nickels")
# cents = cents % CENTS_PER_NICKEL

# print(" ", cents, "pennies")

# ----- Book N15  ------

# I'm using metric system

# m = float(input("m ="))
# cm = m*100
# mm = m*1000
# km = m*0.001
# print(f'km = {km}(km), cm = {cm}(cm), mm = {mm}(mm)')

# ----- Book N14 ------

# foot = float(input("foot ="))
# inch = foot/12
# m = inch/2.54
# print("m =",m)

# ----- Book N16 ------

# r = float(input("r ="))
# import math
# S = math.pi*r**2
# V = math.pi*(r**3)*3/4
# print(f'S={S} (m^2), V = {V} (m^3)')

# ----- Book N17 ------

# m = float(input("m in g ="))
# t = float(input("temperature change ="))
# q = m*4.186*t
# print(f' q = {m*4.186*t}(J)')
# kwh = q * 2.777e-7
# cost = kwh * 8.9
# print(f'energiayi arjeqy = {cost}, ($)')

# ----- Book N18 ------

# r = float(input("r ="))
# h= float(input("h ="))
# import math
# S = math.pi*r**2
# print(f'V = {S*h} (m^3)')

# ----- Book N19 ------

# h = float(input("h in m="))
# g = 9.8 #m/s^2
# import math
# v = math.sqrt(2*g*h)
# print("v =", v, "m/s")

# ----- Book N20 ------

# P = float(input("P ="))
# V = float(input("V ="))
# T = float(input("T in Celsius="))
# T_= T + 273.15 #K
# R = 8.314 #(J/mol*K)
# n = (P*V)/R*T_
# print(f'n = {n} (mol)')

# ----- Book N21 ------

# r = float(input("r ="))
# h= float(input("h ="))
# print(f'S = {r*h/2} (m^2)')

# ----- Book N22 ------

# s1 = float(input("s1 ="))
# s2 = float(input("s2 ="))
# s3 = float(input("s3 ="))
# s = (s1 + s2 + s3)/2
# import math
# print(f'S = {math.sqrt(s*(s - s1)*(s - s2)*(s - s3))} (m^2)')

# ----- Book N23 ------

# s = float(input("s ="))
# n = float(input("n ="))
# import math
# print(f'S = {n*(s**2)/4*math.tan(math.pi/n)}')

# ----- Book N25 during lecture (24) ------

# second_d = 86400
# seconds_h = 3600
# seconds_m = 60

# seconds = int(input("seconds= "))
# d = seconds // second_d
# seconds %= 86400
# h = seconds // seconds_h
# seconds %= 3600
# m = seconds // seconds_m
# seconds %= 60
# result = f' {"%2s" % d}:{"%2s" % h}:{"%2s" % m}:{"%2s" % seconds}'
# result = result.replace(' ','0')
# print(result)

# ----- Book N26 ------
# import datetime
# print(datetime.datetime.now())      

# import time
# print(time.asctime())

# ----- Book N27 ------

# year = int(input("year ="))
# import math
# a = (year / 19 - year//19)
# b = math.floor(year)/100
# c = (year / 100 - year//100)
# d = math.floor(b)/4
# e = b/4 - b//4
# f = math.floor((b+8)/25)
# g = math.floor((b-f+1)/3)
# h = (19*a +b-d-g+14)/30 - (19*a +b-d-g+14)//30
# i = math.floor(c)/4
# k = c/4 -c//4
# l = (32 + 2*e + 2*i -h - k)/7 - (32 + 2*e + 2*i -h - k)//7
# m = math.floor((a+11*h+22*l)/451)
# month = math.floor((h + l -7*m +114)/31)
# day = (h + l - 7*m + 114)/31 - (h + l - 7*m + 114)//31
# print("month", month, "day", day)

# ----- Book N28 ------

# m = float(input("m ="))
# h = float(input("h ="))
# print(f'BMI = {m/h**2}')

# ----- Book N29 ------

# T = float(input("T ="))
# V = float(input("V ="))
# WCI = 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.1

# print(f'WCI = {round(WCI)}')

# ----- Book N30 nman kerp 31------

# T = int(input(" T °C ="))
# print(f'T = {T+273}(K)')

# ----- Book N32 ------

# number = input("4 digit number =")

# digit1 = int(number[0])
# digit2 = int(number[1])
# digit3 = int(number[2])
# digit4 = int(number[3])

# print(f'gumar = {digit1 +digit2 + digit3 + digit4}')

# ----- Book N33 ------
# a = int(input("a  ="))
# b = int(input("b  ="))
# c = int(input("c  ="))

# minimal = min(a,b,c)
# maximal = max(a,b,c)
# middle = a + b + c - minimal - maximal 
# print(minimal, middle, maximal)

# ----- Book N34 ------

# normal_bread = 3.49 #$
# old_bread = normal_bread*0.4
# number = float(input("old bread number ="))
# total_original_prize = number*normal_bread
# total_old_prize = number*old_bread
# print(f'{"%2d" % total_old_prize}\n{"%2d" % total_original_prize}')













