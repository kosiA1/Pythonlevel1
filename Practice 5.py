#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:      Practice 5
# Author:      kosisochi
# Created:     12-12-2020
# Copyright:   (c) anado 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#
for i in "abcdef":
    print (i)

#Range

for i in range(5):
    print (i)

#if range doesnt have a step value, it is automatically [1]
for i in range(2,5):
    print (i)

#in this range below, "1" is the start value, "10" is the stop value, and "2" is the step value.
for i in range(1,10,2):
    print (i)

#if the step is negative, it counts in decending
for i in range(5,1,-1):
    print (i)

#Example 1

a = int(input("Enter a start value: "))
b = int(input("Enter a stop value: "))
c = int(input("Enter a step value: "))

for i in range(a,b,c):
    print(i)

#Example 2

a = int(input("Enter a start value: "))
b = int(input("Enter a stop value: "))

for i in range(a,b+1):
    print(i)
