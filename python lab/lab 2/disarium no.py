# python program to check if given no is disarium number
num = int(input("enter the no "))
rem = s= 0
len =len(str(num))
n= num
while(num>0):
    rem=num%10
    s+=int(rem**len)
    num=num//10
    len-=1
if(s==n):
    print("disarium number")
else:
    print("not a disarium number")

