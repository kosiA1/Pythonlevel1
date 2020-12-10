#-------------------------------------------------------------------------------
# Name:        module 4
# Purpose:     Learning Boolean expression
# Author:      Kosisochi
# Created:     09-12-2020
# Copyright:   (c) anado 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#if boolean expression :
    #statement(s)
#else: (else is only done if the if condition is false)
    #statement(s)

# "if" Example:

a = int(input("Enter a number: "))

if a ==1:
    print("a is 1")
if a != 1:
    print("a is not 1")

color = input("Enter a color: ")

if color == "red":
    print("your color is red")
if color != "red":
    print("your color is not red")

# "else" Example:

color = input("Enter a 2nd color:")

if color == "yellow":
    print("your color is yellow")
else:
    print("your colour is not yellow")

#using "if" and "and"

grade = int(input("Enter a grade: "))

if grade > 80 and grade <= 90:
    print("you met expectations")
    print ("congratulations!")
else:
    print("your grade is off the scale")

#using "if" and "or"[if either of the or conditions are met, if prints]
choice = input("Enter a y: ")
if choice == 'y' or choice =='Y':
    print("you chose y or Y")
else:
    print("you did not choose y or Y")

#NOTE every else line is placed below the "if" line it is for
y = 80

if y >= 50:
    print(y,"is at least 50")
    if y < 60:
        print("but is under 60")
    else:
        print("and at least 60")
else:
    print(y, "is below 50")

# ELIF is a combination of else and if. It can be used as an alternative to else followed by if
x = 80

if x > 50:
    print(x, "is more than 50")
elif x<50:
    print(x, "is less than 50")
else:
    print (x, "is 50")