# python program to print check if given number is happy number

def ishappy(n):
    r =s= 0
    while(n>0):
        r = n%10
        s += r**2
        n//=10
    return s
n =129
res=n 
while(res!=1 and res!=4):
    res=ishappy(res)
if(res==1):
    print("happy number")
elif(res==4):
    print("not a happy number")


