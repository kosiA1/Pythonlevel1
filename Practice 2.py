#-------------------------------------------------------------------------------
# Name:        module 2
# Purpose:     Learning Variables
# Author:      Kosisochi
# Created:     06-12-2020
# Copyright:   (c) anado 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Representing Variables
x = 1
print(x)
print("\n")
name = "Kosisochi"
print(name)
print("\n")
#addition of numbers
sum = 1+2
print (sum)
print("\n")
# addition of Variables
x = 2
y = 4
sum = x + y
print (sum)
print("\n")
#X was 1 and now has been replaced by the second value of x
x = 1
x = 10
print (x)
print("\n")
#adding a string to a print
x = 1
print("The number is", x)
print("\n")

name = "Kosisochi"
print ("The name is", name)
print("\n")

sum = 1+2
print("The sum is", sum)
print("\n")

x = 2
y = 4
sum = x+y
print("The sum is",sum)
print("\n")

x = 1
print ("x is", x)
x = 10
print("x is now", x)

print("\n")
#Input
#input is treated like a sting regardless of what is entered
x = input ("What is your favourite color ")
print ("Your favorite color is", x)
print("\n")

#It returns an empty string
input()

#The input is assigned a variable
x = input()

name = input("What is your name? ")

# .format
#"{placeholder}".format(value)
# {placeholders} is used to specify how many characters of a string is going to show
#{placeholder} is identified with {:.x} "x being whatever number"
print("{}".format(42))
# The placeholder above is empty so it shows all characters
print("\n")
print("{} {} {}".format(42, "Hello World", 10.00))

#These place holders would make only the selected number of Charaters get printed
print("\n")
print("{:.1}".format("Hello World"))
print("{:.3}".format("Hello World"))
print("{:.1}{:.3}".format("Hello","World"))

#using variables
print("\n")
name = "Kosisochi"
number = "123456789"
print("{:.4} {:.3}".format(name,number))
print("My 1st four letters is{:.4}and the 1st three numbers is{:.3}".format(name,number))

