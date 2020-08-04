"""A simple program to compute an integral of a function
using trapezoidal riemann sums
Coded by: Rowan Jansens"""

import math

def main():
    input_f = input('Enter a function (f(x)): ')   #get input function
    lower = int(input('Enter lower bound: '))     #get integral bounds
    upper = int(input('Enter upper bound: '))
    integrate(10000, lower, upper, input_f)
    
def integrate(dx, lower, upper, input_f):
    area = 0
    for i in range(lower, upper):     #iterate through the bounds...
        for j in range(dx):    #...and sub divisions 
            val = ((2 * i) + (j / dx) + ((j + 1) / dx)) / 2  #compute trapezoidal height
            area += (function(val, input_f) * (1 / dx))  #compute trapezoidal area using the functiona and trapezoid height
    print(area)

def function(x, input_f):
    y = eval(input_f)   #evaluate the area using function and heigh
    return y

main()
