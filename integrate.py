"""A simple program to compute an integral of a function
using trapezoidal riemann sums
Coded by: Rowan Jansens"""

import math

def main():
    input_f = input('Enter a python interpretable function (f(x)): ')   #get input function
    lower = int(input('Enter lower bound: '))     #get integral bounds
    upper = int(input('Enter upper bound: '))
    if (lower > upper):  #ensures proper calucation of "backward" integrals
        integrate(upper, lower, input_f, True)   #switch bounds and set "backward" to true
    else:
        integrate(lower, upper, input_f, False)  #or just integrate normally
    
def integrate(lower, upper, input_f, backward):
    area = 0
    dx = 1000   #num sub devisions --> increases accuracy
    for i in range(lower, upper):     #iterate through the bounds...
        for j in range(dx):    #...and sub divisions 
            val = ((2 * i) + (j / dx) + ((j + 1) / dx)) / 2  #compute trapezoidal height
            area += (function(val, input_f) * (1 / dx))  #compute trapezoidal area
    if (backward):
        area *= -1   #switch the sign of backward integrals
    print(area)

def function(x, input_f):
    y = eval(input_f)   #evaluate the input function at given height
    return y

main()
