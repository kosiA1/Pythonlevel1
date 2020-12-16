#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:      Practice 6
# Author:      kosisochi
# Created:     12-12-2020
# Copyright:   (c) anado 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#.Format and Alignment
#[>} - Right align, ( The right align is within 10 spaces)
c = "abc"
d = "def"
print("{:>10}{:>10}".format(c,d))

for i in range(1,11):
    print("{:>10}{:>10}".format(i, i*i))


#[<} - left align, (The right align is within 10 spaces)
x = int(input("Enter a start number: "))
y = int(input("Enter a stop number: "))

for i in range(x,y):
    print("{:<10}{:<10}".format(i,i/2))

#[^] - Center align, (The center align is within 10 spaces)
a = int(input("Enter a 2nd start number: "))
b = int(input("Enter a 2nd stop number: "))

for i in range(a,b):
    print("{:^10}{:^10}".format(i,i+i))