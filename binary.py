import math

def main():
    num = int(input("Enter a number: \n"))
    print(binary_convert(num))

def binary_convert(num): 
    b = {}
    j = int(math.log(get_gf(num)) / math.log(2))

    #make empty dict with the right number of factors
    for i in range(j, -1, -1):
        b[(2 ** i)] = b.get((2 ** i), 0)

    #if a number has gf as a facotr, add 1 to the dict for that factor
    #then decrase the number by that much
    for i in range(len(b)):
        gf = get_gf(num)
        if (gf <= num):
            b[get_gf(num)] = b.get(get_gf(num)) + 1
            num = num - gf
    print(b)
    binary = make_str(b)
    return binary

 #find the largest factor of the order 2^n
def get_gf(num):
    gf = 1
    n = 0
    while (num >= (gf + (2 ** n))):
        gf += (2 ** n)
        n += 1
    return gf

#print the dict as a string from left to right
def make_str(b):
    string = ""
    length = len(b) - 1
    for i in range(length, -1, -1):
        string += str(b[2 ** i])
    return string
     
main()
