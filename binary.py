"""A simple program to convert a number into binary
Coded By: Rowan Jansens"""

import math

def main():
    num = int(input("Enter a number: \n"))   #get number to be converted
    binary_convert(num)

def binary_convert(num): 
    b = []     #make an empty list
    #determine the number of binary factors (2^n) needed to express the input number
    num_factors = int(math.log(get_bf(num)) / math.log(2))   

    #append list with lists of the binary factors calucated above and a value of 0
    for i in range(num_factors, -1, -1):
        b.append([2**i, 0])
    
    for i in range(len(b)):   #loop through the list
        #If the num is larger then the binary factor for current position, change state to 1
        if (num >= b[i][0]):
            b[i][1] = 1
            num -= b[i][0]   #Then update the num by subtracting the factor from it

    make_dict(b)  #print list as dict
    make_str(b)   #print a string of the list values

#find the largest binary factor (of the order 2^n) of the current number
def get_bf(num):
    binary_factor = 1  #smallest factor is always 1
    n = 0
    while (num >= (binary_factor + (2 ** n))):    #increment binary factor by the next factor (2^n) as long as num is larger
        binary_factor += (2 ** n)
        n += 1
    return binary_factor

#print the list as a dictionary
def make_dict(b):
    d = {}
    for i in range(len(b)):
        d.update({int(b[i][0]):int(b[i][1])})
    print(d)

#print the list values as a string
def make_str(b):
    s = ""
    for i in range(len(b)):
        s += str(b[i][1])
    print(s)
     
main()
