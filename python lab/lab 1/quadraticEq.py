#python program to solve the quadratic equation 

import cmath
print("equation is =p mt{a}x**2+{b}x+{c}=0")

a=int(input("a="))
b=int(input("b="))
c=int(input("c"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d)/(2*a))
sol2=(-b+cmath.sqrt(d)/(2*a))

if d>0:
    print("type of root:two distinct real root ")
elif d==0:
    print("type of root: two equal real root ")
elif d<0:
    print("type of root:two complex root  ")
