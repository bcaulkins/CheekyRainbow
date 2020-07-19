# This is version 0.1 of my DiceWare pass phrase generator.                                                                               #
# Use this to quickly generate a secure pass phrase using the DiceWare method shown here: http://world.std.com/~reinhold/diceware.html    #
# Caution: It is recomended to use actual dice and not a digital tool to generate your diceware pass phrase.                              #
# I wanted to see if I could write a program that would achive the same results as rolling dice. This was purely a learning exercise.     #
# Please use at your own risk                                                                                                             #
#                                                                                                                                         #
# Author: Brian Caulkins                                                                                                                  #
# Date: 7/18/2020                                                                                                                         #
###########################################################################################################################################

import random
import re

#Asks user how many words they need.

pwlen = input("How many words do you want? \n")

#Opens the diceware dictionary in readonly mode
DWL = open("diceware_list.txt", "r")
dw_search = DWL.read().split("\n")

#Takes the input and passes into the while loop, which then crudely generates a random number between 1 and 6 and stores them in 1 of 5 variables
#It then searches the diceware dictionary file and finds a matching line, removes spaces and the first 5 digits, fianlly storing that in an array
k=0
a = []
while (k < int(pwlen)):
    num1 = random.randrange(1,7)
    num2 = random.randrange(1,7)
    num3 = random.randrange(1,7)
    num4 = random.randrange(1,7)
    num5 = random.randrange(1,7)

    LookupVal = str(num1)+str(num2)+str(num3)+str(num4)+str(num5)

    for item in dw_search:
            if LookupVal in item:
                mystring = item.strip()
                phrase1 = re.sub(r"[\n\t\s]*", "", mystring)
                a.append(phrase1[5:])
                k = k+1

#prints the array as a string, joining each item in the array with a space for easy reading
print(' '.join(map(str, a)))
