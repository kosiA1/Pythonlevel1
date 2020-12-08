#-------------------------------------------------------------------------------
# Name:        module 3
# Purpose:     Learning Variables
# Author:      Kosisochi
# Created:     08-12-2020
# Copyright:   (c) anado 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Use of Operators and expressions in python [+,-,*,/]

print (2+2)
print (3-2)
print (2*3)
print (4/2)

print("\n")
#PEMDAS is used to know which equation to do first

print (2+3-1)

print ("\n")
# [//] finds the quotient

print(5//2)

print("\n")
#[%] gives the remainder

print (5%2)

#Type conversions

a = input("Enter a number: ")
b = input("Enter a second number: ")
c = a+b
print("The sum is", c)
#Reason for the output is that anything entered as an input is treated as a string
print("\n")
#use [int] to make it recognized as a number

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = a+b
print("The sum is", c)

#int can also be used to convert from string to integer

a = input("Enter a number: ")
b = input("Enter a second number: ")
c = int(a)+ int(b)
print("The sum is", c)

print("\n")
#using float

a = float(input("Enter a number: "))
b = float(input("Enter a second number: "))
c = a+b
print("The sum is", c)

print("\n")
#.format for float "{:.f}"
a = float(2.567)
print("{:.2f}".format(a))
