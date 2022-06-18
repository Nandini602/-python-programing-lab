# python program to print the pronic number between 1 to 100
# pronic nunber is the product of two consecutive integer

import math
print("pronic numbers between 1 to 100 are:")
for n in range(1,101):
    for i in range(int(math.sqrt(n))+1):
        if i*(i+1)==n:
            print(n)
            break